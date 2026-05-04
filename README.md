# 📊 Análise de Vendas com Python e Pandas

Projeto de análise de dados voltado para extração de insights a partir de um conjunto de vendas. O objetivo é demonstrar habilidades práticas em manipulação e análise de dados utilizando **Python** e **Pandas**.

---

## 🚀 Objetivo

Transformar dados brutos de vendas em informações úteis para tomada de decisão, como:

* Identificar os produtos mais lucrativos
* Analisar o faturamento por categoria
* Organizar dados para visualização e relatórios

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Pandas

---

## 📂 Estrutura do projeto

```
analise-vendas-pandas/
│
├── arquivo_csv/
│   └── arquivo.csv              # Dados brutos de entrada
│
├── arquivo_analise/
│   ├── Arquivo_analisado.csv   # Dados com faturamento e ordenação
│   └── Arquivo_faturamento_categoria.csv  # Faturamento por categoria
│
├── analise_vendas.py           # Script principal de análise
└── README.md
```

---

## 📊 Etapas da análise

O script realiza as seguintes operações:

1. Leitura do arquivo CSV com dados de vendas
2. Criação da coluna `faturamento` (`preco * quantidade`)
3. Ordenação dos produtos por faturamento (maior → menor)
4. Agrupamento por categoria com cálculo de faturamento total
5. Identificação do produto com maior faturamento
6. Exportação dos resultados para arquivos `.csv`

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Daguilajairo/Analise-Vendas-Pandas_Python.git
cd Analise-Vendas-Pandas_Python
```

### 2. Instale as dependências

```bash
pip install pandas
```

### 3. Execute o script

```bash
python analise_vendas.py
```

---

## 📈 Exemplo de insights gerados

* Produtos com maior impacto no faturamento
* Categorias mais lucrativas
* Organização dos dados para análise estratégica

---

## 💡 Possíveis melhorias

* Adicionar visualizações com Matplotlib ou Seaborn
* Criar dashboards interativos (ex: Streamlit)
* Implementar análise temporal de vendas
* Aplicar métricas mais avançadas (ticket médio, margem, etc.)

---

## 👨‍💻 Autor

**Jairo Daguila**

* Interesse em Análise de Dados, Finanças e Desenvolvimento
* Foco em evolução contínua e projetos práticos

---

## 📌 Observação

Este projeto faz parte do meu processo de aprendizado em análise de dados, com foco em aplicar conceitos na prática e construir um portfólio sólido.
