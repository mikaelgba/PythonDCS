#Importando o pacote DataTime, aplicações de data e hora
import datetime


# In[2]:
# datetime.datetime.now() retorna a data e o horario atual
hora_agora = datetime.datetime.now()
print(hora_agora)
print("\n")


# In[8]:
# datetime.time() cria um horario
hora_agora2 = datetime.time(5,7,8,1562)
print("Hora(s): ", hora_agora2.hour)
print("Minuto(s): ", hora_agora2.minute)
print("Segundo(s): ", hora_agora2.second)
print("Mini segundo(s): ", hora_agora2.microsecond)
print("\n")


# In[11]:
print(datetime.time.min)
print("\n")


# In[16]:
# datetime.date.today() retorna a data atual
hoje = datetime.date.today()
print(hoje)
print("Hora(s): ", hoje.ctime())
print("Minuto(s): ", hoje.year)
print("Segundo(s): ", hoje.month)
print("Mini segundo(s): ", hoje.day)
print("\n")


# In[20]:
#Criando uma data com o datetime.date()
data1 = datetime.date(2019,12,31)
print("Dia: ", data1)
print("\n")


# In[21]:
#Alterando a data com replace(year='x'), replace(month='x'), replace(day='x')
data2 = data1.replace(year=2020)
print(data2)
# In[22]:
print(data2 - data1)
# In[ ]:


