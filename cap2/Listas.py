
lista1 = ["Eu, Você, e  o Zubumafu"]

lista2 = ["Fogo","Água","Terra","Ar","Raio","Metal"]

print(lista1, "\n")

#Separando os indices da lista2
print(lista2[0])
print(lista2[1])
print(lista2[2])
print(lista2[3], "\n")

# alterando o elemento da String
print(lista1)
lista1[0] = "Eu, Você, e  o Zubumafu para sempre"
print(lista1, "\n")

# Deletar o elemento da String
lista2 = ["Fogo","Água","Terra","Ar","Raio","Metal"]
del lista2[5]
print(lista2, "\n")

# Retornar o elemento da String
b = lista2[0]
print(b, "\n")

lista3 = [["Mu","Aiolia","Aiolos"],["Aldebaran","Shaka","Shura"],["Saga","Dorko","Kamus"],["Mascará da Morte","Miro","Afodite"]]
print(lista3, "\n")

# Manipulando o elemento de um indice
lista3 = [["Mu","Aiolia","Aiolos"],["Aldebaran","Shaka","Shura"],["Saga","Dorko","Kamus"],["Mascará da Morte","Miro","Afodite"]]
a = lista3[0][2] + " Melhor cavaleiro"
print(a, "\n")

a = lista3[0]
b = lista3[1]
c = lista3[2]
d = lista3[3]
print( a, b, c, d, "\n")

# Verificando se um o elemento esta na lista
print("Mu" in lista3[0], "\n")

# Verificando tamanho da lista
print(len(lista3), "\n")

# Verificando o valor maximo entre os elementods da lista
lista4 = [5,8,2,10,5]
print(max(lista4), "\n")

# Verificando o valor minimo entre os elementods da lista
lista4 = [5,8,2,10,5]
print(min(lista4), "\n")

lista4.append(3)
print(lista4, "\n")

# Adicionando um elemento em um indice desejado na lista
lista4.insert(2,7)
print(lista4, "\n")

# Adicionando um elemento pelo indice 
lista4.remove(2)
print(lista4, "\n")

# Ordenando a lista do menor para o maior
lista4.sort()
print(lista4, "\n")

print(lista4.count(5), "\n")

list = ["Fogo","Água","Terra","Ar","Raio","Metal"]
list.extend (["Nuvem","Energia"])
print(list, "\n")

print((list.index("Terra")), "\n")

