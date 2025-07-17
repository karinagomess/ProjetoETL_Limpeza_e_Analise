import pandas as pd
import pyodbc

# 1. Leitura do arquivo CSV
date_frame = pd.read_csv("vendas_julho_2025.csv", sep=";", encoding="utf-8-sig")

print("arquivo lido com sucesso!")
print("colunas encontradas: ", date_frame.columns.tolist()) # Mostrar colunas encontradas


# 2. Limpeza e Tranformação 
date_frame["Total_Venda"] = date_frame["Quantidade"] * date_frame["Preco_Unitario"] # criar coluna Total_Venda
date_frame["Lucro_Bruto"] = (date_frame["Preco_Unitario"] - date_frame["Custo_Unitario"]) * date_frame["Quantidade"] # criar coluna Lucro_Bruto
date_frame["Data_Venda"] = pd.to_datetime(date_frame["Data_Venda"],  format="%d/%m/%Y") # formatar data

print("colunas adicionadas: ", date_frame.columns.tolist()) # Mostrar colunas adicionadas

# Padronizar Valores
data = {'Forma_Pagamento': ['boleto', 'Cartao de Debito', 'cartao de debito', 'Cartao de Credito',
                              'cartao de credito', 'dinheiro', 'pix']}# Exemplo de DataFrame
df = pd.DataFrame(data)

# Dicionário de correção para padronização
correcoes = {
    'boleto': 'Boleto',
    'cartao de credito': 'Cartão de Crédito',
    'Cartao de credito' : 'Cartão de Crédito',
    'cartao de debito': 'Cartão de Débito',
    'cartao de debito': 'Cartão de Débito',
    'dinheiro': 'Dinheiro',
    'pix': 'PIX'
}

# Função para padronizar
df['Forma_Pagamento'] = df['Forma_Pagamento'].str.lower().replace(correcoes)
# print(df) Apenas para visualizar a correção


# 3. Conectar ao Banco de dados SQL Server
server = "KARINAGOMES" # ou o seu servidor
database = 'db_VendasJulho2025' # nome do Banco de dados
conexao = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;') # Validar conexão
cursor = conexao.cursor() # Conectar


# 4. Criar tabela
cursor.execute("""
IF OBJECT_ID('dbo.VendasJulho2025', 'U') IS NULL
    CREATE TABLE dbo.VendasJulho2025 (
        ID_Venda INT PRIMARY KEY,
        Data_Venda DATE,
        Loja VARCHAR(50),
        Produto VARCHAR(100),
        Categoria VARCHAR(50),
        Quantidade INT,
        Preco_Unitario FLOAT,
        Vendedor VARCHAR(100),
        Forma_Pagamento VARCHAR(50),
        Custo_Unitario FLOAT,
        Total_Venda FLOAT,
        Lucro_Bruto FLOAT
    );
""")


# 5. Inserir os dados
for index, linha in date_frame.iterrows():
    cursor.execute("""
        INSERT INTO dbo.VendasJulho2025 (ID_Venda, Data_Venda, Loja, Produto, Categoria, Quantidade,
            Preco_Unitario, Vendedor, Forma_Pagamento, Custo_Unitario, Total_Venda, Lucro_Bruto)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",

        linha['ID_Venda'], linha['Data_Venda'], linha['Loja'], linha['Produto'], linha['Categoria'],
        linha['Quantidade'], linha['Preco_Unitario'], linha['Vendedor'], linha['Forma_Pagamento'],
        linha['Custo_Unitario'], linha['Total_Venda'], linha['Lucro_Bruto'])


# Commit para salvar as alterações no banco de dados
conexao.commit()

# Fechar a conexão
cursor.close()
conexao.close()

print("Dados inseridos com sucesso!")