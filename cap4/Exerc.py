# 1
#forma 1 da 1
lista = [1,2,3,4,5]
lista2 = []
for i in lista:
    a = i**3
    lista2.append(i)
print(lista2)
print("\n")

#forma 2 da 1
retorno = [i**3 for i in lista]
print(retorno)
print("\n")

#2
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
saida = map(lambda w: [w.upper(), w.lower(), len(w)],palavras)
for i in saida:
    print(i)
print("\n")

#3
#forma 1 da 3
matrix = [[1, 2],[3,4],[5,6],[7,8],[9,10]]
lista_transpot = []
a = []
b = []
for i in range(len(matrix[0])):
    lista_transpot.append([matrix[j][i] for j in range(len(matrix))])
'''    a.append(i[0])
    b.append(i[1])
lista_transpot.append(a)
lista_transpot.append(b)'''
print(lista_transpot)
print("\n")

#forma 2 da 3
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
print("\n")

#4
#forma 1 da 4
def quad(x):
    return x**2
def cub(x):
    return x**3
for i in lista:
    print(quad(i), ":",cub(i))
print("\n")

#forma 2 da 4
funcs = [quad,cub]
for i in lista:
    valor = map(lambda x: x(i), funcs)
    print(list((valor)))
print("\n")

#5
list1 = [2,3,4]
list2 = [10,11,12]
#forma 1 da 5
for i in range(len(list1)): print(list1[i] ** list2[i])
print("\n")

#forma 2 da 5
print(list(map(pow,list1,list2)))
print("\n")

#6
print(list(filter(lambda i: i < 0,range(-10,10))))
print("\n")

#7
l1 = [1,2,3,4,5,6]
l2 = [1,3,5]
print(list(filter(lambda l2: l2 in l1,l2)))
print("\n")

#8
import time
print(time.strftime("%Y %b %d %a %H:%M:%S"))
print("\n")

#9
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

troca = list(zip(dict1,dict2.values()))
print(troca,"\n")

#10
lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lista_letras[6:])
