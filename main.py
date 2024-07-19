import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx')

# tirar limite de colunas visiveis
pd.set_option('display.max_columns', None)

# faturamento por loja // filtra colunas // agrupa e soma
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print('-' * 30)
#ticket médio por produto em cada loja
# to_frame() transforma em tabela de dados
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)

