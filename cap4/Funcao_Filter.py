#Criando uma função para verificar se um numero é impar
def ver_impar(numero): 
    if ((numero % 2) != 0): 
        return True 
    else: 
        return False
    
print(ver_impar(10), "\n")


#Criando uma lista adicionando nela valores randomicos
import random
# a se torna em uma lista com 10 varoles random
a = random.sample(range(100),10)
print(a)
print("\n")


# In[ ]:
print(filter(ver_impar,a))
print("\n")


# In[ ]:
#imprimindo o retorno da função com os valores apenas imapres
print(list(filter(ver_impar,a)))
print("\n")



# In[ ]:
#Ultilixando o filter com lambda
print(list(filter(lambda x: (x % 2) == 0, a)))
print("\n")
print(list(filter(lambda x: x >= 50, a)))

