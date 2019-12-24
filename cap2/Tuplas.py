tupla1 = ("a",1,"c")
print(tupla1)

print(tupla1[0])

#Retorna o tamanho da tupla
print(len(tupla1))

#Retorna o indice de um elemento
print(tupla1.index("c"))

#Deleta uma tupla
del tupla1

tupla2 = (1,2,3)
print(tupla2)

#Converte uma Tupla em Lista
tupla_aux = list(tupla2)
print(tupla_aux)

tupla_aux.append(4)
print(tupla_aux)

#Converte uma Lista em Tupla
tupla2 = tuple(tupla_aux)
print(tupla2)
