from pandas import Series
from pandas import DataFrame
from matplotlib import style
import pandas as pd
import numpy as np
import matplotlib as plt
import sys
import os

dataset = {'Sigla' : ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES',
                      'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PE',
                      'PE', 'PE', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
                      'SP', 'SE', 'TO',],
           'Estado' : ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia',
                       'Ceara', 'Distrito Federal', 'Espírito Santo',
                       'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso',
                       'Mato Grosso do Sul', 'Minas Gerais', 'Pará',
                       'Paraíba', 'Pernambuco', 'Piauí', 'Rio de Janeiro',
                       'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia',
                       'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe',
                       'Tocantins',],
           'População' : [732793, 3120922, 668689, 3480937, 14021432,
                          8448.055, 2562963, 3512672, 6004045, 6569683,
                          3033.991, 2449341, 19595309, 7588078, 3766834,
                          10439.601, 8796032, 3119015, 15993583, 3168133,
                          10695.532, 1560501, 6341000, 6249682, 41252160,
                          2068031, 1383453]}

   
# vai tornar a variavel "dataset" do tipo dicionario para um dataframe
estados = pd.DataFrame(dataset)
print("Estados do Brasil", "\n", estados, "\n")

# é possivel a criacao de funcoes para amanipulacao dos dados
def cresce_popu(quantidade):
    return quantidade + (quantidade * 0.2)

estados["População"] = estados["População"].apply(cresce_popu)
print("Crecimento da população generico", "\n", estados, "\n")


linguagens = ["C","C++","C#","Java","JavaScript","Python","R","Ruby"]
# Atribuindo nome de colunas com o parâmetro "columns"
linguagens_aux = pd.DataFrame(linguagens, columns=["Liguagens"])
print(linguagens_aux, "\n")

#Adicao de uma nova colina
linguagens_aux["Ano Criação"] = [1972, 1985 , 1999, 1991, 1996, 1991, 1993, 1993] 
print(linguagens_aux, "\n")


# Análise de dados com Pandas:
nome = "arquivos/titanic/titanic.csv"
tit = pd.read_csv(nome)

# head() -> retorna as primeiras (por padrão 5) linhas do dataframe
print("Topo do DataFrame", "\n", tit.head(), "\n")
#mas pode ser a quantidade que desejar
print("Topo do DataFrame", "\n", tit.head(10), "\n")

# tail() -> retorna as ultimas (por padrão 5) linhas do dataframe
print("Fim do DataFrame", "\n", tit.tail(), "\n")
#mas tambem pode ser a quantidade que desejar
print("Fim do DataFrame", "\n", tit.tail(10), "\n")

# describe() -> retorna dados estatísticos sobre o Dataframe
print("Descrição do DataFrame", "\n",tit.describe(), "\n")


# Ordenação dos dados
# sort_values(by = "nome da coluna") -> Ordenando em ordem crescente
tit.sort_values(by = "Name")
print("ordem crescente", "\n", tit, "\n")

# sort_values(by = "nome da coluna", ascending = False) -> Ordenando em ordem decrescente
tit.sort_values(by = "Name", ascending = False) 
print("ordem decrescente", "\n", tit, "\n")


# Resumo dos dados
# sum() -> retorna a soma dos valores do DataFrame
print("Soma dos Valores:", "\n", tit.sum(), "\n")
# Soma dos valores de uma(as) coluna(as) espefici
print("Soma das Idades:", "\n", tit["Age"].sum(), "\n")

# min() -> retorna o menor valor do DataFrame
print("Menor valor:", "\n", tit.min(), "\n")
# Menor valor de uma(as) coluna(as) espeficia
print("Menor Idade:", "\n", tit["Age"].min(), "\n")

# max() -> retorna a maior valor
print("Maior valor:", "\n", tit.max(), "\n")
# Maior valor de uma(as) coluna(as) espeficia
print("Maior Idade:", "\n", tit["Age"].max(), "\n")

# mean() -> retorna a média dos valores
print("Média:", "\n", tit.mean(), "\n")
# Média de uma(as) coluna(as) espeficia
print("Média Idade:", "\n", tit["Age"].mean(), "\n")

# median() -> retorna a mediana dos valores
print("Mediana:", "\n", tit.median(), "\n")
# Mediana de uma(as) coluna(as) espeficia
print("Mediana Idade:", "\n", tit["Age"].median(), "\n")


# Informações básicas
# shape -> retorna uma tupla contendo a size de linhas e colunas
print("Size \n", tit.shape, "\n")

# index -> descricao do Index
print("Descrição \n", tit.index, "\n")

# columns -> colunas presentes no DataFrame
print("Nome das Colunas \n", tit.columns, "\n")

# count() -> contagem de dados nao nulos
print("Total de pessoas no Navio \n", tit.count(), "\n")
# contagem de uma(as) coluna(as) espefica
print("Size Coluna Age \n", tit["Age"].count(), "\n")


# Filtragem de dados #
# novo_dataframe = dataframe[dataframe["coluna"] "Operecao" com "O quevocê quer comparar"]
tit2 = tit[tit["Sex"] == "male"]
tit3 = tit[tit["Sex"] == "female"]
print("Size \n", tit2, "\n", tit3, "\n")

# Filtragem pela idade dos sobreviventes
tit4 = tit[tit["Age"] > 30]
tit4 = tit4[tit4["Survived"] == 1]
print("Size \n", tit4, "\n")

# como padrao, mesmo nao colocando os indices em uma Series o pandas coloca o index da Series
serie_um = Series([10,20,30,40])
print(serie_um, "\n", serie_um.values, "\n", serie_um.index, "\n")

# Series([10,20,30,40], index = ["a","b","c","d"]) -> Colocando indices em uma Series
serie_dois = Series([10,20,30,40], index = ["a","b","c","d"])
print(serie_dois, "\n", serie_dois.values, "\n", serie_dois.index, "\n")

# Series permitem a uma leitura facil dos dados em fragmentos
# seguindo certos paramentos de exclusao
print(serie_dois[serie_dois.index != "b"], "\n")
print(serie_dois[serie_dois.values < 30], "\n")

print("d" in serie_dois, "\n")

# Posso criar um dicionario e passar para uma Series como paramentro
dicio = {"Mu": [1, "Aries"], "Aldebaran": [2, "Touro"], "Saga": [3, "Gemios"],  "Mascará da Morte": [4, "Cancer"],
         "Aiolia": [5, "Leao"], "Shaka" : [6, "Virgem"], "Dorko": [7, "Libra"], "Miro": [8, "Escopiao"],
         "Aiolos": [9, "Sagitario"], "Shura": [10, "Capriconio"], "Kamus": [11, "Aquario"], "Afodite": [12, "Peixes"]}

serie_tres = Series(dicio)
print(serie_tres, "\n")

dicio_dois = {"User 1": "Michael", "User 2": "Mago", "User 3": "Implacavel", "User 4": "Supremo", "User 5": "Lendario"}
lista = ["User 1", "User 2", "User 3", "User 4", "User 6"]
serie_quatro = Series(dicio_dois, index = lista)
print(serie_quatro, "\n")

# Ao ultilizar Series necessario atencao nos indices 
# para evitar a criacao de elementos nulos, como no exemplo abaixo
# User 1       Michael
# User 2          Mago
# User 3    Implacavel
# User 4       Supremo
# User 6           NaN

# pd.isnull(Series) -> retorna se ha elementos nulos 
print(pd.isnull(serie_quatro))

serie_quatro.name = "Users"
serie_quatro.index.name = "Users"
print(serie_quatro)

# DATAFRAMES - >>>
data = {'Sigla' : ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES',
                      'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PE',
                      'PE', 'PE', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
                      'SP', 'SE', 'TO',],
           'Estado' : ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia',
                       'Ceara', 'Distrito Federal', 'Espírito Santo',
                       'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso',
                       'Mato Grosso do Sul', 'Minas Gerais', 'Pará',
                       'Paraíba', 'Pernambuco', 'Piauí', 'Rio de Janeiro',
                       'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia',
                       'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe',
                       'Tocantins',],
           'População' : [732793, 3120922, 668689, 3480937, 14021432,
                          8448.055, 2562963, 3512672, 6004045, 6569683,
                          3033.991, 2449341, 19595309, 7588078, 3766834,
                          10439.601, 8796032, 3119015, 15993583, 3168133,
                          10695.532, 1560501, 6341000, 6249682, 41252160,
                          2068031, 1383453]}


# Criando um dataframe
dataframe_um = DataFrame(data)
print(dataframe_um.head(), "\n")

# Ordernando as colunas de um DataFrame
dataframe_dois = DataFrame(data, columns=["Estado", "Sigla", "População"])
print(dataframe_dois, "\n")

# Adicionando uma nova coluna
dataframe_tres = DataFrame(data, columns = ["Estado", "Sigla", "População", "Numero Estado"],
                          index = np.arange(27))
print(dataframe_tres, "\n")

dataframe_tres[:5]

# Adicionando dados na coluna Numero Estado
dataframe_tres["Numero Estado"] = np.arange(27) + 1
print(dataframe_tres, "\n")

print(dataframe_tres.values, "\n \n", dataframe_tres["População"].describe(), "\n")

print(dataframe_tres["População"] >= 10000000, "\n")

print(dataframe_tres[0:5], "\n")

# Localiza pelo parametro de entrada
print(dataframe_tres.loc[10], "\n")

# Localiza pelo Indice
print(dataframe_tres.iloc[10], "\n")

dicio_tres = {"Nome" : ["Mu", "Aldebaran", "Saga", "Mascará da Morte", "Aiolia", "Shaka", 
                        "Dorko", "Miro", "Aiolos", "Shura", "Kamus", "Afodite"], 
              "Cavaleiro" : ["Aries", "Touro", "Gemios", "Cancer", "Leao", "Virgem", 
                             "Libra", "Escopiao", "Sagitario", "Capriconio", "Aquario", "Peixes"],
              "Numero da casa" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}

dataframe_quatro = pd.DataFrame(dicio_tres)
print(dataframe_quatro, "\n")

print(dataframe_quatro["Cavaleiro"], "\n")

print(dataframe_quatro[["Nome", "Cavaleiro"]], "\n")

print(dataframe_quatro.set_index("Numero da casa"), "\n")

arquivo_csv = '../cap4/arquivosUsados1/salarios.csv'
dframe = pd.read_csv(arquivo_csv)
print(dframe, "\n")

tita_dois = pd.read_csv('../cap4/arquivosUsados1/salarios.csv', names = ["Nome","Cargo","Departamento","Salario"])
print(tita_dois, "\n")
# se quiser salvar as alteracoes basta fazer -> tita_dois.to.csv(sys.stdout, sep = ";")
# na parte do -> sep = ";", voce pode usar qualquer caracter para fazer a separacao

# -> pd.date_range('20200523', periods = 10), Cria uma usando uma data e uma quantidade de periodos
dados_criado = pd.date_range('20200523', periods = 10)
# Ejetando dados neste dataframe 
daframe = pd.DataFrame(np.random.randn(10,4), index = dados_criado, columns = list("ABCD")) 
print(daframe, "\n")

d_um = pd.DataFrame({"Chave" : ["Chave 1", "Chave 2 "], "Itens 1" : [1,3]})
d_dois = pd.DataFrame({"Chave" : ["Chave 1", "Chave 2 "], "Itens 2" : [2,4]})
# merclar dois ou mais dataframes -> pd.merge(dataframe1, dataframe2, on = "paramentro de juncao")
print(pd.merge(d_um, d_dois, on = "Chave"))

d_tres = pd.DataFrame(np.random.randn(20,4), columns = ["A","B","C","D"]) 
aux_d = d_tres.iloc[3]
print(aux_d)

print(d_tres.append(aux_d, ignore_index= True))

# TIME SERIES - >>>
# freq = "M" é a frequencia por mes, S = segundos, Y = anos e etc...
dt = pd.date_range('23/05/2020', periods = 50, freq = "S")
# Alimentando a a serie temporal com elementos randomicos 
dados_ts = pd.Series(np.random.randint(-100, 100, len(dt)), index = dt) 
print(dados_ts)

dt_dois = pd.date_range('23/05/2020', periods = 50, freq = "M")
# Alimentando a a serie temporal com elementos randomicos 
dados_ts_dois = pd.DataFrame(np.random.randn(len(dt_dois)), index = dt_dois) 
print(dados_ts_dois)

# Plotting - >>>
dados_ts_tres = pd.Series(np.random.randn(100), index = pd.date_range('23/05/2020', periods = 100))
dados_ts_tres = dados_ts_tres.cumsum()
dados_ts_tres.plot()

dados_df_tres = pd.DataFrame(np.random.randn(100, 4), index = dados_ts_tres.index, columns = ["WARNER BROS",
                                                                                              "UNIVERSAL PICTURES",
                                                                                              "COLUMBIA/SONY",
                                                                                              "20TH CENTURY FOX"])
dados_df_tres = dados_df_tres.cumsum()
plt.figure; dados_df_tres.plot()

# OUTUPUT - >>>
#dados_df_tres.to_excel('arq-studio.xlsx', sheet_name = "Sheet1")
dados_df_tres.to_excel('arq_studio.xlsx', sheet_name='Sheet1')
novo_arq = pd.read_excel('arq_studio.xlsx', 'Sheet1', index_col = None, na_values=["NA"])
print(novo_arq.head())

os.remove('arq_studio.xlsx')
