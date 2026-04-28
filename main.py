import pandas as pd
from estrutura_de_dados import dados_vendas

df = pd.DataFrame(dados_vendas)

# 1.  Calculando o faturamento total por linha

df["Faturamento_total"]= df['Preco_Unitario'] *df['Quantidade_Vendida']

# 2. Vendas totais por vendedor

vendas_por_vendedor = df.groupby('Vendedor')['Faturamento_total'].sum().sort_values(ascending=False)

# 3. produtos com estoque baixo

estoque_critico = df[df['Estoque_Atual']<5][['Produto','Estoque_Atual']]

print("--- Resumo de Vendas por Vendedor ---")
print(vendas_por_vendedor)
print("\n--- Alerta de Estoque Crítico ---")
print(estoque_critico)