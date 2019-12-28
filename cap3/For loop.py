tupla = ("a","b","c")
for i in tupla:
    print(i)

lista_letras = ["a","b","c"]
for i in lista_letras:
    print(i)

for i in lista_letras:
    if( i == "c"):
        print("Há o valor 'c' na lista")

#Imprimir entre um intervalo 
for contador in range(0,5):
    print(contador)

#Imprimir entre um intervalo de 2 em 2 usando a função RANGE
for contador in range(0,50,2):
    print(contador)

#Imprimir os elementos pares da lista
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if(i % 2 == 0 ):
        print(i)

a = "Saint Seiya"
for i in a:
    print(i)

#For loop aninhado
for i in range(0,10):
    for j in range(0,10):
        print( i + 1, "X", j + 1, "=", (i + 1) * (j + 1))

lista2 = [10,20,30,40,50,60,70]
soma = 0
for i in lista2:
    soma += i
print(soma)

#Imprimir as sublistas separadas
lista_aux = [["a","b","c"],["d","e","f"],["h","i","j"]]
for i in lista_aux:
    print(i)

#Imprimir os elementos das sublistas em sequência
for i in lista_aux:
    for j in i:
        print(j)

lista_aux = [["a","b","c"],["d","e","f"],["h","i","j"]]
quant_colunas = 0 #ou também, poderia ser quant_colunas = lista_aux[0]
for i in lista_aux:
    quant_colunas += 1
print(quant_colunas)

#imprimir os valores do Dicionario
dicio = {1:"Python",2:"Java",3:"C#",4:"Ruby"}
for i in dicio.values():
    print(i)

#imprimir as chaves do Dicionario
for i in dicio.keys():
    print(i)

#imprimir as chaves e os elementos do Dicionario
for i,j in dicio.items():
    print(i,j)

#Função RANGE - for in in range(x,y,z) 
#X: é o valor inicial
#Y: o valor maximo/final
#Z: o intervalo/salto
for i in range(0,10,2):
    print(i)

for i in range(0,-10,-2):
    print(i)

lista_aux2 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(lista_aux2)):
    print(lista_aux2[i])

#Tudo em Python é um objeto
type(range(0,3))
