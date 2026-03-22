import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("vendas.csv")

# Criar coluna de faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

# Faturamento total
faturamento_total = df["faturamento"].sum()
print("Faturamento total:", faturamento_total)

# Produtos mais vendidos
produtos = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
print("\nProdutos mais vendidos:")
print(produtos)

# Faturamento por categoria
categoria = df.groupby("categoria")["faturamento"].sum()

# Gráfico
categoria.plot(kind="bar", title="Faturamento por Categoria")
plt.show()
