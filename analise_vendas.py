import pandas as pd

df = pd.read_csv("arquivo_csv/arquivo.csv")

df["faturamento"] = df["preco"] * df["quantidade"]
ordenacao = df.sort_values(by="faturamento",ascending=False)
print(ordenacao)

print("__________________________________________________")

faturamento_categoria = df.groupby("categoria")["faturamento"].sum().reset_index()
print("FATURAMENTO POR CATEGORIA")
print(faturamento_categoria)


print("__________________________________________________")
maior_faturamento = df[df["faturamento"]==df["faturamento"].max()]
print("PRODUTO COM MAIOR FATURAMENTO")
print(maior_faturamento)


ordenacao.to_csv("arquivo_analise/Arquivo_analisado.csv",index=False)
faturamento_categoria.to_csv("arquivo_analise/Arquivo_faturamento_categoria.csv",index=False)