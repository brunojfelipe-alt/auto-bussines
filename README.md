# AutoBusiness

Projeto simples de **automação de análise de vendas usando Python**.

O objetivo deste projeto é demonstrar um fluxo básico de automação de dados:

* leitura de arquivos CSV
* limpeza e organização dos dados
* geração de métricas
* criação de gráficos
* exportação de dados consolidados

---

# Funcionalidades

O script realiza automaticamente:

* leitura de múltiplos arquivos CSV
* consolidação dos dados em um único DataFrame
* cálculo de faturamento total
* geração de gráficos de vendas
* exportação de um CSV com os dados consolidados

---

# Tecnologias utilizadas

* Python
* pandas
* matplotlib
* sys
* pathlib

---

# Estrutura do projeto

```
auto_business
│
├── script.py
├── dados_exemplo
│   ├── vendas_loja1.csv
│   ├── vendas_loja2.csv
│
├── output
│
└── README.md
```

---

# Como usar

1. Clone o repositório

```
git clone https://github.com/brunojfelipe-alt/auto-business.git
```

2. Entre na pasta do projeto

```
cd auto-business
```

3. Execute o script passando a pasta com os dados

```
python script.py dados_exemplo
```

---

# Saída do programa

O script irá:

* gerar gráficos de vendas
* calcular métricas
* salvar um arquivo CSV consolidado

Os arquivos gerados são salvos na pasta **output**.

---

# Objetivo do projeto

Este projeto foi desenvolvido como exercício prático de:

* automação de planilhas
* manipulação de dados
* criação de scripts reutilizáveis em Python
