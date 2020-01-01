#  Enumerate retorna uma lista de elementos e seus indices
a = [1,2,3,4,5,6,7,8,9,10]
enumerate(a)
print(list(enumerate(a)))
print("\n")


# In[ ]:
#Retorna os elementos e seus indices
for indice,valor in enumerate(a):
    print(indice,valor)
print("\n")


# In[ ]:
#Retorna os elementos e seus indices até um indice expecifico
for indice,valor in enumerate(a):
    if( indice > 3):
        break
    else:
        print(indice,valor)
print("\n")


# In[ ]:
#Retorna os indices e elementos de uma lista
lista = ["Obi Wan","Yoda","Luck"]
for x,y in enumerate(lista):
    print(x,y)
print("\n")


# In[ ]:
#Retorna os indices e elementos de uma String
for x,y in enumerate("Castlevania"):
    print(x,y)
print("\n")


# In[ ]:
#Retorna os indices e os indices de range()
for x,y in enumerate(range(11)):
    print(x,y)

