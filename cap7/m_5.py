import pandas as pd
import numpy as np

arquivo = "dataset/dados_compras.json"
leitura = pd.read_json(arquivo, orient = "records")
print(leitura,"\n")

#1 Informações Sobre os Consumidores
info_compradores = leitura.loc[:,["Login","Sexo","Idade"]]
print("Informações Sobre os Consumidores", "\n", info_compradores,"\n","\n")


#2 Análise Geral de Compras
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

print("Análise Geral de Compras", "\n", leitura["Item ID"].unique(),"\n")
print("Análise Geral de Compras", "\n", dicio_compras,"\n")

#2.3 manipulação/tratamento dos dados
#dicio_compras = dicio_compras.round(2)
dicio_compras ["Preco medio"] = dicio_compras["Preco medio"].map("${:,.2f}".format)
dicio_compras["Valor total dos Itens"] = dicio_compras["Valor total dos Itens"].map("${:,.2f}".format)
dicio_compras = dicio_compras.loc[:, ["Itens unico",
                                      "Preco medio",
                                      "Valor total dos Itens",
                                      "Numero total de Itens"]]

print("Análise Geral de Compras", "\n",dicio_compras,"\n","\n")


#3 Informações Demográficas
#3.1 Cálculos básicos
quant_clientes = info_compradores.count()[0]
genero = info_compradores["Sexo"].value_counts()
genero_porc = (genero / quant_clientes) * 100

#3.2 Dataframe para os resultados
genero_analise = pd.DataFrame({"Sexo" : genero,
                               "%" : genero_porc})
#3.3 manipulação/tratamento dos dados
genero_analise["%"] = genero_analise["%"].map("{:,.1f}%".format)
print("Porcetagem de Generos", "\n", genero_analise, "\n","\n")


#4 Análise de Compra Por Gênero
#4.1 Coletando dados
gender_total_item_price = leitura.groupby(["Sexo"]).sum()["Valor"].rename("Total de Vendas")
gender_average_item_price = leitura.groupby(["Sexo"]).mean()["Valor"].rename("Average Price")
purchase_count = leitura.groupby(["Sexo"]).count()["Valor"].rename("Número de Compras")
normalized_total = gender_total_item_price / genero_analise["Sexo"]

#4.2 Novo Dataframe
comprar_por_genero = pd.DataFrame({"Número de Compras" : purchase_count,
                                   "Valor Médio Por Item" : gender_average_item_price,
                                   "Total de Vendas" : gender_total_item_price,
                                   "Total Normalizado" : normalized_total})

#4.3 manipulação/tratamento dos dados
comprar_por_genero = comprar_por_genero.round(2)
comprar_por_genero["Valor Médio Por Item"] = comprar_por_genero["Valor Médio Por Item"].map("${:,.2f}".format)
comprar_por_genero["Total de Vendas"] = comprar_por_genero["Total de Vendas"].map("${:,.2f}".format)
comprar_por_genero["Total Normalizado"] = comprar_por_genero["Total Normalizado"].map("${:,.2f}".format)

print("Análise de Compras Por Gênero", "\n", comprar_por_genero["Total de Vendas"], "\n")
print("Análise de Compras Por Gênero", "\n", comprar_por_genero,"\n","\n")


#5 Análise Demográfica Idade
#5.1 cricao de listas auxiliares
idade_bins = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 999]
faixa_idade = ["Até 10", "10 - 14",
               "15 - 19", "20 - 24", "25 - 29",
               "30 - 34", "35 - 39", "Maior que 40"]

leitura["Range de Idades"] = pd.cut(leitura["Idade"], idade_bins, labels = faixa_idade)

#5.2 coletagem de dados
intervalo_idade = leitura["Range de Idades"].value_counts()
valor_de_unidade = leitura.groupby(["Range de Idades"]).mean()["Valor"]
valor_total = leitura.groupby(["Range de Idades"]).sum()["Valor"]
porcetagem_idade = (intervalo_idade / quant_clientes) * 100

#5.3 Novo Dataframe
analise_idade = pd.DataFrame({"Contagem": intervalo_idade,
                              "%": porcetagem_idade,
                              "Valor Unitario": valor_de_unidade,
                              "Valor Total de Compra": valor_total})

#5.4 Data Munging
analise_idade["Valor Unitario"] = analise_idade["Valor Unitario"].map("${:,.2f}".format)
analise_idade["Valor Total de Compra"] = analise_idade["Valor Total de Compra"].map("${:,.2f}".format)
analise_idade["%"] = analise_idade["%"].map("{:,.2f}%".format)
'''analise_idade = analise_idade.sort_index()'''
print("Análise Demográfica Idade", "\n", analise_idade,"\n","\n")


#6 Top Spenders
#6.1 coletagem de dados
total_compras_user = leitura.groupby(["Login"]).sum()["Valor"].rename("Valor Total")
media_compra = leitura.groupby(["Login"]).mean()["Valor"].rename("Valor Médio")
quant_compras = leitura.groupby(["Login"]).count()["Valor"].rename("Número de Compras")
idade = leitura["Idade"]

#6.2 Novo Dataframe
user_compras = pd.DataFrame({"Valor Total": total_compras_user,
                             "Valor Médio": media_compra,
                             "Número de Compras": quant_compras})

#6.3 Data Munging
user_compras["Valor Total"] = user_compras["Valor Total"].map("${:,.2f}".format)
user_compras["Valor Médio"] = user_compras["Valor Médio"].map("${:,.2f}".format)
print("Usuarios que mais compram", "\n", user_compras.sort_values("Valor Total", ascending = False).head(5), "\n")
print("Usuarios que mais compram", "\n", user_compras, "\n","\n")


#7 Itens Mais Populares
#7.1 coletagem de dados
item_total = leitura.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor Total")
item_media = leitura.groupby(["Nome do Item"]).mean()["Valor"].rename("Valor Médio")
item_count = leitura.groupby(["Nome do Item"]).count()["Valor"].rename("Número de Compras")

#7.2 Novo Dataframe
itens_data = pd.DataFrame({"Valor Total": item_total,
                           "Valor Médio": item_media,
                           "Número de Compras": item_count})

#7.3 Data Munging
itens_data ["Valor Total"] = itens_data["Valor Total"].map("${:,.2f}".format)
itens_data ["Valor Médio"] = itens_data["Valor Médio"].map("${:,.2f}".format)
print("Itens Mais Populares", "\n", itens_data.sort_values("Número de Compras", ascending=False).head(5), "\n")
print("Itens Mais Populares", "\n", itens_data, "\n","\n")


#8 Itens Mais Lucrativos
#8.1 coletando
user_total = leitura.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor Total")
user_average = leitura.groupby(["Nome do Item"]).mean()["Valor"].rename("Valor Médio")
user_count = leitura.groupby(["Nome do Item"]).count()["Valor"].rename("Número de Compras")

#8.2 Novo Dataframe
user_data = pd.DataFrame({"Valor Total": user_total,
                          "Valor Médio": user_average,
                          "Número de Compras": user_count})

#8.3 Data Munging
user_data ["Valor Total"] = user_data["Valor Total"]
user_data ["Valor Total"] = user_data["Valor Total"].map("${:,.2f}".format)
user_data ["Valor Médio"] = user_data["Valor Médio"].map("${:,.2f}".format)


print("Itens Mais Lucrativos", "\n",
      user_data.sort_values("Valor Total",
                            ascending=False).head(5)[['Valor Total',
                                                      'Valor Médio',
                                                      'Número de Compras']])
