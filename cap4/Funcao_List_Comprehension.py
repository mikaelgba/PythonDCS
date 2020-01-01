#Retorna uma lista com cada caractere em uma sequencia de caracteres 
list1 =[ x for x in "Yoda"]
print(list1)
print("\n")

print(type(list1))
print("\n")


# In[ ]:
list2 =[ x**2 for x in range(11)]
print(list2)
print("\n")


# In[ ]:
#List comprehension com condicionais
list3 =[ x for x in range(11) if (x % 2) != 0]
print(list3)
print("\n")


# In[ ]:
#List comprehension aninhados
list4 = [ x**2 for x in [ x**2 for x in range(11)]]
print(list4)

