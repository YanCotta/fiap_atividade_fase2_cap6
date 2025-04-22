import json
import cx_Oracle
from datetime import datetime

# Constantes
VALOR_IDEAL_MATURACAO = 18.0  # Índice mínimo de maturação para colheita

# Função para calcular a data ideal de colheita
def calcular_data_colheita(dados_maturacao):
    for data, indice in dados_maturacao:
        if indice >= VALOR_IDEAL_MATURACAO:
            return data
    return None

# Função para alocar colhedoras
def alocar_colhedoras(colhedoras_disponiveis, areas_a_colher):
    alocacao = {}
    colhedoras = colhedoras_disponiveis.copy()
    for area in sorted(areas_a_colher, key=lambda x: x[1], reverse=True):
        for colhedora in colhedoras:
            if colhedora[1] >= area[1]:
                alocacao[area[0]] = colhedora[0]
                colhedoras.remove(colhedora)
                break
    return alocacao

# Função para salvar dados em JSON
def salvar_dados_json(dados, arquivo="colheita.json"):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para carregar dados de JSON
def carregar_dados_json(arquivo="colheita.json"):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para conectar ao banco Oracle e inserir dados
def inserir_dados_banco(data_colheita, perda_estimada):
    try:
        connection = cx_Oracle.connect(user="seu_usuario", password="sua_senha",
                                       dsn="localhost:1521/xe")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO colheitas (data_colheita, perda_estimada) VALUES (:1, :2)",
                       (data_colheita, perda_estimada))
        connection.commit()
        cursor.close()
        connection.close()
        print("Dados salvos no banco com sucesso!")
    except cx_Oracle.Error as e:
        print(f"Erro ao conectar ao banco: {e}")

# Função para validar entrada numérica
def validar_numero(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                print("Digite um valor positivo!")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número.")

# Interface de usuário
def main():
    dados_maturacao = []
    colhedoras_disponiveis = []
    areas_a_colher = []

    while True:
        print("\n=== Sistema de Gestão de Colheita ===")
        print("1. Adicionar dados de maturação")
        print("2. Calcular data ideal de colheita")
        print("3. Adicionar colhedora")
        print("4. Adicionar área a colher")
        print("5. Alocar colhedoras")
        print("6. Salvar dados em JSON")
        print("7. Carregar dados de JSON")
        print("8. Salvar colheita no banco")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Data (DD/MM/YYYY): ")
            try:
                datetime.strptime(data, "%d/%m/%Y")
                indice = validar_numero("Índice de maturação: ")
                dados_maturacao.append((data, indice))
                print("Dados adicionados com sucesso!")
            except ValueError:
                print("Data inválida! Use o formato DD/MM/YYYY.")

        elif opcao == "2":
            if not dados_maturacao:
                print("Nenhum dado de maturação cadastrado!")
            else:
                data_ideal = calcular_data_colheita(dados_maturacao)
                if data_ideal:
                    print(f"Data ideal para colheita: {data_ideal}")
                else:
                    print("Nenhum dado atingiu o índice ideal de maturação.")

        elif opcao == "3":
            id_colhedora = input("ID da colhedora: ")
            capacidade = validar_numero("Capacidade (toneladas): ")
            colhedoras_disponiveis.append((id_colhedora, capacidade))
            print("Colhedora adicionada com sucesso!")

        elif opcao == "4":
            id_area = input("ID da área: ")
            tamanho = validar_numero("Tamanho (toneladas): ")
            areas_a_colher.append((id_area, tamanho))
            print("Área adicionada com sucesso!")

        elif opcao == "5":
            if not colhedoras_disponiveis or not areas_a_colher:
                print("Cadastre colhedoras e áreas antes de alocar!")
            else:
                alocacao = alocar_colhedoras(colhedoras_disponiveis, areas_a_colher)
                if alocacao:
                    print("Alocação de colhedoras:")
                    for area, colhedora in alocacao.items():
                        print(f"Área {area} -> Colhedora {colhedora}")
                else:
                    print("Não foi possível alocar todas as áreas.")

        elif opcao == "6":
            salvar_dados_json(dados_maturacao)
            print("Dados salvos em colheita.json!")

        elif opcao == "7":
            dados_maturacao = carregar_dados_json()
            print("Dados carregados:", dados_maturacao)

        elif opcao == "8":
            data_colheita = input("Data da colheita (DD/MM/YYYY): ")
            try:
                datetime.strptime(data_colheita, "%d/%m/%Y")
                perda = validar_numero("Perda estimada (%): ")
                inserir_dados_banco(data_colheita, perda)
            except ValueError:
                print("Data inválida! Use o formato DD/MM/YYYY.")

        elif opcao == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()