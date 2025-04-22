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
Este projeto foi desenvolvido como parte da atividade avaliativa da disciplina de Gestão do Agronegócio em Python. Utilizando princípios avançados de programação orientada a objetos e arquitetura modular, criamos uma solução tecnológica robusta para otimizar a colheita mecânica de cana-de-açúcar, visando reduzir as perdas que podem chegar a 15% da produção.

## Arquitetura do Sistema
O projeto segue uma arquitetura modular com separação clara de responsabilidades:

```
src/
├── config/           # Configurações do sistema
│   └── database.py   # Configurações do banco de dados
├── database/         # Camada de persistência
│   └── db_handler.py # Gerenciamento de conexão com Oracle
├── models/           # Modelos de domínio
│   └── colheita.py   # Classes principais do sistema
├── utils/            # Utilitários
│   └── helpers.py    # Funções auxiliares
└── main.py          # Ponto de entrada da aplicação
```

## Funcionalidades Principais

### 1. Gestão de Áreas
- Cadastro georreferenciado de áreas de cultivo
- Monitoramento de índices de maturação
- Cálculo automático de prioridade de colheita

### 2. Gerenciamento de Colhedoras
- Cadastro e monitoramento de equipamentos
- Controle de capacidade e manutenção
- Sistema inteligente de alocação

### 3. Otimização de Colheita
- Algoritmo de priorização baseado em múltiplos fatores
- Integração com dados geográficos
- Minimização de perdas na colheita

### 4. Persistência de Dados
- Armazenamento local em JSON para configurações
- Banco de dados Oracle para histórico e análises
- Sistema de logging para auditoria

## Tecnologias Utilizadas

### Backend
- Python 3.x
- Oracle Database
- Bibliotecas:
  - cx_Oracle: Integração com banco de dados
  - dataclasses: Modelagem de dados
  - logging: Sistema de logs
  - json: Persistência local

### Ferramentas de Desenvolvimento
- Git: Controle de versão
- VS Code: IDE principal
- Oracle SQL Developer: Gerenciamento do banco

## Instalação e Configuração

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados:
- Crie um banco Oracle
- Configure as credenciais em `src/config/database.py`

4. Execute o sistema:
```bash
python src/main.py
```

## Uso do Sistema

### Cadastro de Áreas
```python
# Exemplo de cadastro de área
area = AreaColheita(
    id="A001",
    tamanho=50.0,  # hectares
    indice_maturacao=18.5,
    data_medicao=datetime.now(),
    localizacao={'lat': -23.5505, 'lon': -46.6333}
)
```

### Alocação de Colhedoras
O sistema automaticamente:
1. Avalia índices de maturação
2. Considera distâncias geográficas
3. Otimiza a distribuição de equipamentos

## Monitoramento e Logging
- Logs detalhados de operações
- Rastreamento de eficiência
- Histórico de colheitas

## Contribuição
Para contribuir com o projeto:
1. Faça um Fork
2. Crie uma branch para sua feature
3. Faça commit das alterações
4. Push para a branch
5. Abra um Pull Request

## Referências
- SOCICANA: Perdas na colheita de cana-de-açúcar
- Blog CHB Agro: <https://blog.chbagro.com.br/perdas-na-colheita-de-cana-voce-sabe-como-reduzi-las>

## Licença
Este projeto está sob a licença MIT.