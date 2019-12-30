#Dando o nome do Arquivo
nome_Arqui = input("Nome: ")
nome_Arqui +=".txt"
print(nome_Arqui)

#Criando um arquivo e depois lendo ele
arqui = open(nome_Arqui,"w")
arqui.write("Criando um Arquivo")
arqui.close()
arqui = open(nome_Arqui,"r")
print(arqui.read())
arqui.close()

#Lendo o arquivo e fazendo por divisão de linha
arq = open("arquivosUsados1/salarios.csv","r")
a = arq.read()
linha = a.split("\n")
print(linha)

#Lendo o arquivo e fazendo por divisão de linha
arq = open("arquivosUsados1/salarios.csv","r")
a = arq.read()
linhas = a.split("\n")
lista_linhas = []
for linha in linhas:
    linha_unica = linha.split(",")
    lista_linhas.append(linha_unica)
for i in range(len(lista_linhas)):
    print(lista_linhas[i])
        #print(lista_linhas[i])

#Contando as linhas do arquivo
contador = 0
for i in lista_linhas:
    contador += 1
print(contador)

#Contando as colunas do arquivo
contador2 = 0
colunas = lista_linhas = [0]
for linha in colunas:
    contador =+ 1
print(contador2)
arq.close()

#Criando um arquivo e depois lendo ele
nome_Arquiv = "test_arquivo.txt"
arqu = open(nome_Arquiv,"w")
arqu.write("Criando um Arquivo")
arqu.close()

arq2 = open("arquivosUsados1/test_arquivo.txt","r")
arq2.read()
print(arq2.read())
#seek() server para voltar ao inicio do arquivo
arq2.seek(0)

#Ler como arquivo dividindo as linhas por indices
arq2.seek(0)
print(arq2.readlines())

#Ler com o Loop For para ler
for i in open("arquivosUsados1/test_arquivo.txt"):
    print(i)
arq2.close()

#Pacote pandas, Importando e lendo Datasets com pandas
import pandas as pd
nome_arquivo = "arquivosUsados1/binary.csv"
df = pd.read_csv(nome_arquivo)
print(df.head())

#Lndo o arquivo salarios.csv com pandas
nome_arquivo2 = "arquivosUsados1/salarios.csv"
df = pd.read_csv(nome_arquivo2)
print(df.head())




