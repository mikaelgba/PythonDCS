import pandas  as pd

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

# Base de dados
tita = pd.read_csv("arquivos/titanic/titanic.csv")
print(tita.plot.area(figsize=(12, 4), subplots = True))

