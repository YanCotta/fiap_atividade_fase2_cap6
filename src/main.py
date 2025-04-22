"""
Sistema de Gestão da Colheita de Cana-de-Açúcar
Módulo principal da aplicação
"""
import sys
from datetime import datetime
from models.colheita import GerenciadorColheita, Colhedora, AreaColheita
from database.db_handler import DatabaseHandler
from utils.helpers import (
    configurar_logging,
    validar_data,
    carregar_json,
    salvar_json,
    calcular_eficiencia_colheita,
    validar_coordenadas
)
import logging

class SistemaColheita:
    def __init__(self):
        configurar_logging()
        self.logger = logging.getLogger(__name__)
        self.gerenciador = GerenciadorColheita()
        self.db = DatabaseHandler()
        self.carregar_dados()

    def carregar_dados(self):
        """Carrega dados salvos do sistema."""
        dados = carregar_json('dados_sistema.json')
        if dados:
            self.logger.info("Dados do sistema carregados com sucesso")

    def salvar_dados(self):
        """Salva dados do sistema."""
        dados = {
            'areas': [vars(area) for area in self.gerenciador.areas],
            'colhedoras': [vars(colhedora) for colhedora in self.gerenciador.colhedoras]
        }
        if salvar_json(dados, 'dados_sistema.json'):
            self.logger.info("Dados do sistema salvos com sucesso")

    def cadastrar_area(self):
        """Interface para cadastro de nova área."""
        try:
            id_area = input("ID da área: ")
            tamanho = float(input("Tamanho da área (hectares): "))
            indice = float(input("Índice de maturação atual: "))
            data_str = input("Data da medição (DD/MM/YYYY): ")
            data = validar_data(data_str)
            
            lat = float(input("Latitude da área: "))
            lon = float(input("Longitude da área: "))
            
            if not validar_coordenadas(lat, lon):
                raise ValueError("Coordenadas geográficas inválidas")

            area = AreaColheita(
                id=id_area,
                tamanho=tamanho,
                indice_maturacao=indice,
                data_medicao=data,
                localizacao={'lat': lat, 'lon': lon}
            )
            self.gerenciador.adicionar_area(area)
            print("Área cadastrada com sucesso!")
            self.logger.info(f"Nova área cadastrada: {id_area}")
            
        except ValueError as e:
            print(f"Erro no cadastro: {e}")
            self.logger.error(f"Erro ao cadastrar área: {e}")

    def cadastrar_colhedora(self):
        """Interface para cadastro de nova colhedora."""
        try:
            id_colhedora = input("ID da colhedora: ")
            capacidade = float(input("Capacidade de colheita (ton/dia): "))
            
            colhedora = Colhedora(id=id_colhedora, capacidade=capacidade)
            self.gerenciador.adicionar_colhedora(colhedora)
            print("Colhedora cadastrada com sucesso!")
            self.logger.info(f"Nova colhedora cadastrada: {id_colhedora}")
            
        except ValueError as e:
            print(f"Erro no cadastro: {e}")
            self.logger.error(f"Erro ao cadastrar colhedora: {e}")

    def realizar_alocacao(self):
        """Realiza a alocação de colhedoras às áreas."""
        alocacao = self.gerenciador.alocar_colhedoras()
        if alocacao:
            print("\nAlocação de colhedoras:")
            for area_id, colhedora_id in alocacao.items():
                print(f"Área {area_id} -> Colhedora {colhedora_id}")
            self.logger.info(f"Alocação realizada com sucesso: {len(alocacao)} áreas alocadas")
        else:
            print("Não foi possível realizar alocações no momento.")
            self.logger.warning("Tentativa de alocação sem áreas ou colhedoras disponíveis")

    def registrar_colheita(self):
        """Registra os dados de uma colheita realizada."""
        try:
            area_id = input("ID da área colhida: ")
            colhedora_id = input("ID da colhedora utilizada: ")
            producao = float(input("Produção total (toneladas): "))
            perda = float(input("Perda estimada (%): "))
            data_str = input("Data da colheita (DD/MM/YYYY): ")
            data = validar_data(data_str)

            dados_colheita = {
                'data_colheita': data,
                'area_id': area_id,
                'colhedora_id': colhedora_id,
                'producao_total': producao,
                'perda_estimada': perda
            }

            if self.db.salvar_colheita(dados_colheita):
                print("Colheita registrada com sucesso!")
                self.logger.info(f"Colheita registrada para área {area_id}")
            else:
                print("Erro ao registrar colheita no banco de dados.")

        except ValueError as e:
            print(f"Erro no registro: {e}")
            self.logger.error(f"Erro ao registrar colheita: {e}")

    def menu_principal(self):
        """Menu principal do sistema."""
        while True:
            print("\n=== Sistema de Gestão da Colheita de Cana-de-Açúcar ===")
            print("1. Cadastrar Nova Área")
            print("2. Cadastrar Nova Colhedora")
            print("3. Realizar Alocação de Colhedoras")
            print("4. Registrar Colheita")
            print("5. Visualizar Áreas Prioritárias")
            print("6. Salvar Dados do Sistema")
            print("7. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.cadastrar_area()
            elif opcao == "2":
                self.cadastrar_colhedora()
            elif opcao == "3":
                self.realizar_alocacao()
            elif opcao == "4":
                self.registrar_colheita()
            elif opcao == "5":
                areas_prioritarias = self.gerenciador.calcular_prioridade_colheita()
                if areas_prioritarias:
                    print("\nÁreas Prioritárias para Colheita:")
                    for area in areas_prioritarias:
                        print(f"Área {area.id} - Índice de Maturação: {area.indice_maturacao}")
                else:
                    print("Não há áreas prontas para colheita no momento.")
            elif opcao == "6":
                self.salvar_dados()
            elif opcao == "7":
                print("Salvando dados e encerrando...")
                self.salvar_dados()
                sys.exit(0)
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    sistema = SistemaColheita()
    sistema.menu_principal()