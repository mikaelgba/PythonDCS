import pandas as pd
import numpy as np

arquivo = "dataset/dados_compras.json"
leitura = pd.read_json(arquivo, orient = "records")
print(leitura)

#1 Informações Sobre os Consumidores
info_compradores = leitura.loc[:,["Login","Sexo","Idade"]]
print(info_compradores)

#2 Análise Geral de Compras
info_compras = leitura.loc[:,["Login","Sexo","Idade"]]
#2.1 coletando dados do dataframe original
precos_itens = leitura["Valor"].mean()
total_valor = leitura["Valor"].sum()
numero_itens = leitura["Valor"].count()
item_id = len(leitura["Item ID"].unique())

#2.2 Colocando os danos no novo dataframe
dicio_compras = pd.DataFrame({"Itens unico": item_id,
                              "Preco medio":[precos_itens],
                              "Valor total dos Itens":total_valor,
                              "Numero total de Itens":numero_itens})
print(leitura["Item ID"].unique())
print(dicio_compras)
#2.3 manipulação/tratamento dos dados
#dicio_compras = dicio_compras.round(2)
dicio_compras ["Preco medio"] = dicio_compras["Preco medio"].map("${:,.2f}".format)
dicio_compras["Valor total dos Itens"] = dicio_compras["Valor total dos Itens"].map("${:,.2f}".format)
dicio_compras = dicio_compras.loc[:, ["Itens unico",
                                      "Preco medio",
                                      "Valor total dos Itens",
                                      "Numero total de Itens"]]
print(dicio_compras)
