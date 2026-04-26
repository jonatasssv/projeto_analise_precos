import pandas as pd

# Dados fictícios para o seu portfólio
data = {
    'Mercado': ['Trimais', 'Violeta', 'Trimais', 'Violeta'],
    'Produto': ['Arroz', 'Arroz', 'Feijão', 'Feijão'],
    'Preço': [25.90, 24.50, 8.50, 9.10]
}

df = pd.DataFrame(data)

# Uma análise simples: Preço médio por produto
media_precos = df.groupby('Produto')['Preço'].mean()

print("--- Análise de Preços Inicial ---")
print(df)
print("\n--- Média por Produto ---")
print(media_precos)