#Importando a função reduce dentro do pacote functools
from functools import reduce


# In[ ]:
def soma(a,b): return a + b
lista = [15,29,11,57]
print(lista, "\n")


# In[ ]:
#Ultilizando o reduce()
reduce(soma,lista)
print(reduce(soma,lista),"\n")


# In[ ]:
#Ultilizando o reduce() com lambda
print(reduce(lambda a,b: a + b,lista),"\n")


# In[ ]:
#Ultilizando o reduce() com lambda para descobrir o maior valor da lista
maior_valor = lambda a,b: a if (a > b) else b
print(reduce(maior_valor,lista),"\n")


