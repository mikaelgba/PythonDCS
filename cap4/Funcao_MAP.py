def tem_celcius(temperatura): return ((float(9)/5) * (temperatura + 32))

def tem_fahrenheit(temperatura): return ((float(9)/5) * (temperatura - 32))

temps = [50,70,120,29,35]

#A função Map() recebe uma função e uma sequencia, onde ela applica a função de entrada para cada indice da sequencia
print(temps)
print("\n")


# In[ ]:
#Aplicando função biit-in map() com a função tem_celcius na lista temps[]
map(tem_celcius,temps)


# In[ ]:
#Aplicando função biit-in map() com a função tem_fahrenheit na lista temps[]
map(tem_fahrenheit,temps)


# In[ ]:
#Chamando o map() dentro de list() para retorar a lista com os elementos alterados
list(map(tem_celcius,temps))
print(list(map(tem_celcius,temps)))
print("\n")


# In[ ]:
#Chamando o map() dentro de list() para retorar a lista com os elementos alterados
list(map(tem_fahrenheit,temps))
print(list(map(tem_fahrenheit,temps)))
print("\n")


# In[ ]:
#Usando o Lambda dentro da map()
map(lambda entrada: ((9.0)/5) * (entrada + 32), temps)
print(list(map(lambda entrada: ((9.0)/5) * (entrada + 32), temps)))
print("\n")


# In[ ]:
#Usando o Lambda dentro da map() com multiplas listas
list1 = [1,4,7,10]
list2 = [2,5,8,11]
list3 = [3,6,9,12]
map(lambda a,b,c: a + b + c, list1,list2,list3)
print(list(map(lambda a,b,c: a + b + c, list1,list2,list3)))
print("\n")


# In[ ]:
print(list(map(lambda a,b,c: a + b + c, list1,list2,list3)))
# In[ ]:



