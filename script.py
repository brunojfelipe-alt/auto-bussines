import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path
dados = Path(sys.argv[1])
arquivos = list(dados.glob("*.csv"))
dfs = []
for a in arquivos:
    d = pd.read_csv(a)
    dfs.append(d)
df = pd.concat(dfs)
df = df.sort_values("data", ascending= True)
df["produto"] = df["produto"].str.strip()
df["produto"] = df["produto"].str.lower()
df["faturamento"] = df["preco"] * df["quantidade"]
df9 = df.groupby("produto")["quantidade"].sum()
df10 = df.groupby("categoria")["quantidade"].sum()
df11 = df.groupby("data")["faturamento"].sum()
print(f"Faturamento Total = {df["faturamento"].sum()}R$")
x = df9.index
y = df9.values

bars = plt.bar(x, y)
plt.grid(axis="y", linestyle="--", alpha=0.7)
for bar in bars:
    altura = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        altura,
        int(altura),
        ha="center",
        va="bottom"
    )

plt.xticks(rotation=45)

plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.title("Vendas por Produto")
plt.savefig(f"{dados}/grafico_vendas_produto.png")
plt.show()
x = df10.index
y = df10.values

bars = plt.bar(x, y)
plt.grid(axis="y", linestyle="--", alpha=0.7)
for bar in bars:
    altura = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        altura,
        int(altura),
        ha="center",
        va="bottom"
    )

plt.xticks(rotation=45)

plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.title("Vendas por Categoria")
plt.savefig(f"{dados}/grafico_vendas_categoria.png")
plt.show()
x = df11.index
y = df11.values

bars = plt.bar(x, y)
plt.grid(axis="y", linestyle="--", alpha=0.7)
for bar in bars:
    altura = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        altura,
        int(altura),
        ha="center",
        va="bottom"
    )

plt.xticks(rotation=45)

plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.title("Faturamento por Dia")
plt.savefig(f"{dados}/grafico_faturamentos_dia.png")
plt.show()
df.to_csv(f"{dados}/dados_consolidados.csv", index=False)