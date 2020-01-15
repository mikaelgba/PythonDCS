import os

# In[ ]:
import sqlite3
conex = sqlite3.connect('jupyterNotebook/hqs.db')
type(conex)

# In[ ]:
cur = conex.cursor()
type(cur)

# In[ ]:
#Criando a instrucao sql
create_tabela = 'create table hqs''(id integer primary key, ''titulo varchar(100),' 'editora varchar(140))'

# In[ ]:
#Executando a instrucao no cursor
cur.execute(create_tabela)


# In[ ]:
#instrucao para inserir 
insert_tabela = 'insert into hqs values (?,?,?)'

entrada = [(1,"Superman: The Man of Tomorrow","DC"),(2,"Thor: Raknarok","Marvel"),(3,"Green Lantern: Blackest Night","DC")]
#inserindo
for i in entrada:
    cur.execute(insert_tabela, i)


# In[ ]:
#GRAVANDO
conex.commit()

# In[ ]:
#criando instrucao pata recuperar/ler os dados do banco
select_tabela = 'select * from hqs'
cur.execute(select_tabela)
dados_retorno = cur.fetchall()


# In[ ]:


#mostar os dados recuperados
for i in dados_retorno:
    print(i)


# In[ ]:


#ou
for i in dados_retorno:
    print("ID: %d - HQ: %s - Empresa: %s " %i)


# In[ ]:


conex.close()





