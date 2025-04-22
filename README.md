# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sistema de Gestão da Colheita de Cana-de-Açúcar

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/yan-cotta/">Yan Cotta</a>

## 👩‍🏫 Professores:
### Tutor(a)
- Lucas Gomes Moreira 
### Coordenador(a)
- André Godoi Chiovato

## Informações do Aluno

- **Nome**: Yan Pimentel Cotta
- **RM**: 562836
- **Fase**: 2
- **Capítulo**: 7

## Introdução
Este projeto foi desenvolvido como parte da atividade avaliativa da disciplina de Gestão do Agronegócio em Python. O objetivo é criar uma solução tecnológica que auxilie na redução das perdas na colheita mecânica de cana-de-açúcar, um problema significativo no agronegócio brasileiro. Segundo estudos, as perdas na colheita mecânica podem chegar a 15%, representando prejuízos financeiros expressivos. Este sistema propõe otimizar o planejamento, o monitoramento da maturação e a alocação de colhedoras para minimizar essas perdas.

## Problema Tratado
O foco desta solução é abordar as altas perdas na colheita mecânica de cana-de-açúcar, um setor em que o Brasil é líder mundial. A mecanização, embora inevitável e eficiente em escala, aumenta as perdas em comparação à colheita manual (5%). A solução visa:
- Determinar o momento ideal de colheita com base em dados de maturação.
- Otimizar a alocação de colhedoras para maximizar a eficiência.
- Armazenar e consultar dados históricos para suportar decisões futuras.

## Solução Proposta
O sistema foi implementado em Python e inclui os seguintes módulos:
1. **Planejamento da Colheita**: Calcula o momento ideal de colheita com base em índices de maturação.
2. **Gestão de Colhedoras**: Aloca colhedoras de forma eficiente, considerando capacidade e demanda.
3. **Armazenamento de Dados**: Usa arquivos JSON para configurações e um banco de dados Oracle para dados históricos.
4. **Interface de Usuário**: Permite interação via prompt de comando, com validação de entradas.

### Tecnologias Utilizadas
- **Subalgoritmos**: Funções e procedimentos com passagem de parâmetros para modularizar a lógica.
- **Estruturas de Dados**: Listas para séries temporais, tuplas para colhedoras, e dicionários para parâmetros de cana.
- **Manipulação de Arquivos**: Arquivos JSON para salvar e carregar dados de maturação.
- **Conexão com Banco de Dados**: Integração com Oracle para armazenar históricos de colheita.

## Como Executar
1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca `cx_Oracle` instalada (`pip install cx_Oracle`).
   - Banco de dados Oracle configurado com as credenciais fornecidas no código.
2. **Passos**:
   - Clone o repositório GitHub.
   - Execute o arquivo `main.py` no terminal: `python main.py`.
   - Siga as instruções no prompt para interagir com o sistema.

## Inovação
A solução propõe uma abordagem integrada que combina análise de dados de maturação com gestão logística de colhedoras, algo essencial para reduzir perdas na colheita mecânica. A conexão com banco de dados permite escalabilidade e uso de dados históricos para previsões futuras, alinhando-se às tendências de agrotechs.

## Estrutura do Código
- `main.py`: Arquivo principal com a lógica do sistema e interface de usuário.
- `colheita.json`: Arquivo gerado para armazenar dados de maturação.

## Exemplo de Uso
1. Insira dados de maturação (data e índice) para determinar o momento ideal de colheita.
2. Cadastre colhedoras e áreas a colher para receber uma alocação otimizada.
3. Consulte ou salve dados no banco de dados Oracle.

## Referências
- SOCICANA: Perdas na colheita de cana-de-açúcar.
- Blog CHB Agro: <https://blog.chbagro.com.br/perdas-na-colheita-de-cana-voce-sabe-como-reduzi-las>.