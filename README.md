# 📊 Projeto ETL - Análise de Vendas de uma Rede Varejista

### 🚀 Simulação Real de um Desafio de Analista de BI Júnior

---

## 📁 Sobre o Projeto

Este projeto foi desenvolvido como uma simulação prática de um cenário real enfrentado por analistas de Business Intelligence em empresas do setor varejista. 
O objetivo foi construir uma solução completa — da ingestão de dados ao dashboard interativo — capaz de transformar dados brutos em insights estratégicos para auxiliar gestores na tomada de decisões.

---

## 🎯 Desafio

A empresa fictícia forneceu um arquivo com dados de vendas realizados por diversas lojas ao longo de 30 dias. Como analista de BI, fui responsável por:

- Automatizar o processo de ingestão, transformação e carga dos dados (ETL);
- Estruturar os dados em um banco relacional (SQL Server);
- Desenvolver um dashboard no Power BI para análise de KPIs e tendências;
- Garantir a clareza, interatividade e capacidade de filtro nas visualizações.

---

## 🗃️ Fonte de Dados

- **Arquivo fornecido**: `vendas_simuladas_julho_2025_com_custo.csv`
- **Quantidade de registros**: 6.000 linhas
- **Período**: Julho de 2025
- **Colunas disponíveis**:
  - ID_Venda
  - Data_Venda
  - Loja
  - Produto
  - Categoria
  - Quantidade
  - Preço Unitário
  - Custo Unitário
  - Vendedor
  - Forma de Pagamento

---

## ⚙️ Processo ETL

O processo de ETL foi realizado em Python com as seguintes etapas:

1. **Extração**:
   - Leitura dos dados a partir do arquivo CSV fornecido pela empresa.

2. **Transformação**:
   - Cálculo do **Total da Venda** (`Quantidade * Preço Unitário`);
   - Cálculo do **Lucro Bruto** (`(Preço - Custo) * Quantidade`);
   - Padronização de campos como *Forma de Pagamento* e *Categoria*;
   - Conversão e tratamento do campo de data.

3. **Carga**:
   - Inserção dos dados tratados na tabela `dbo.VendasJulho2025` no SQL Server.

---

## 📊 Visualização no Power BI

Com base nos dados estruturados no banco, foi construído um dashboard interativo que responde às seguintes **perguntas de negócio**:

### 🧠 Perguntas Respondidas:

- Qual foi o faturamento total no mês?
- Qual foi o lucro bruto total?
- Qual o ticket médio das vendas?
- Qual loja mais vendeu?
- Qual categoria de produto gerou mais lucro?
- Quem são os melhores vendedores?
- Quais formas de pagamento são mais utilizadas?
- Como evoluíram as vendas ao longo dos dias?

---

## 📌 Principais Visões do Dashboard

- **KPIs principais**: Total de Vendas, Lucro Bruto, Ticket Médio, Total de Produtos Vendidos
- **Gráficos de Tendência**: Vendas e Lucro por Dia
- **Comparativos**:
  - Por Loja
  - Por Categoria
  - Por Vendedor
- **Análise de Produto Mais Vendido**
- **Distribuição por Forma de Pagamento**
- **Filtros Interativos**: Dia, Vendedor, Categoria, Produto

> 🖼️ O dashboard foi desenvolvido com foco em clareza, escalabilidade e aplicação prática em ambientes corporativos.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Pandas, Faker, SQLAlchemy
- **SQL Server**: Modelagem de banco relacional e carga de dados
- **Power BI**: Criação de dashboards dinâmicos com KPIs, filtros e análises comparativas

---

## Imagem do Dashboard

<img width="1305" height="729" alt="Captura de tela 2025-07-17 105131" src="https://github.com/user-attachments/assets/b3a1467b-a442-4351-81fb-58254019839e" />

---

## 📎 Conclusão

Este projeto demonstra minha capacidade de atuar como Analista de BI em um cenário realista, entregando valor ao negócio por meio da integração entre dados, automação e visualização.

---

## 👩‍💻 Sobre Mim

Sou Karina Gomes, profissional em início de carreira com foco em análise de dados e Business Intelligence. Estou disponível para oportunidades como:

- **Analista de BI Júnior**

- **Trainee em Dados**
- **Analista de Dados Iniciante**

🔗 [LinkedIn](#https://www.linkedin.com/in/karina-gomes-8b6b4a2a8)

---

## Autora

Karina Gomes
