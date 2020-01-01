#Criando 2 listas para aplicarno zip()
a = [1,2,3]
b = [4,5,6]
zip(a,b)
print(list(zip(a,b)))
print("\n")


# In[ ]:
#Zip() retorna com o tamanho da lista com menor numero de elementos 
c = list(zip("abcd","ab"))
print(c)
print("\n")


# In[ ]:
# 2 Dcionarios para os testes
d = {"jedi": ["Obi Wan","Yoda","Luck"], "sith": ["Lord maul","Dark Vader","Darth Sidious"]}
e = {1: "Personagens a: ", 2:"Personagens b: "}
#Retorna apenas as chaves
f = list(zip(e,d))
print(f)
print("\n")


# In[ ]:
#Retorna apenas as chaves
g = list(zip(e.values(),d.values()))
print(g)
print("\n")


# In[ ]:
#Fazendo a troca do valores de D para as chevas de E
h = list(zip(e.values(),d))
print(h)
print("\n")


# In[ ]:
#Retornando as chaves e valores de D e E
i = list(zip(e.items(),d.items()))
print(i)

