import sqlite3
import random
import matplotlib.pyplot as plt

conexao = sqlite3.connect("jupyterNotebook/id_random.db")
cur = conexao.cursor()

def create_tabela():
    
    criar_sql = ("CREATE TABLE IF NOT EXISTS id_random(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, valor REAL)")
    cur.execute(criar_sql)
    
def insert_tabela(lista_entrada):
    
    inserir_sql = ("INSERT INTO id_random VALUES(?,?)")
    for i in lista_entrada:
        cur.execute(inserir_sql, i)
    conexao.commit()
 
def select_tabela():
    
    select_sql = "select * from id_random"
    cur.execute(select_sql)
    retorno = cur.fetchall()
    for i in retorno:
        print(i)
    conexao.commit()

def select_tabela2():
    
    select_sql = "select id, valor from id_random"
    cur.execute(select_sql)
    ids = []
    salarios = []
    retorno = cur.fetchall()
    for i in retorno:
        ids.append(i[0])
        salarios.append(i[1])
    plt.bar(ids,salarios)
    plt.show()

def update_tabela(atual, menor_que):
    
    update_sql = "UPDATE id_random SET valor = ? WHERE valor < ?"
    up = (atual, menor_que)
    cur.execute(update_sql,up)
    conexao.commit()

def delete_indice(dele):
    
    dele_sql = "DELETE FROM id_random WHERE valor < ?"
    cur.execute(dele_sql, (dele,))
    conexao.commit()

#Criando   
create_tabela()

lista_random = []
for i in range(20):
    a = random.uniform(1039, 15000)
    lista_random.append([i + 1,a])
    
print(lista_random)

#Inserindo
insert_tabela(lista_random)
select_tabela()
select_tabela2()

#Atualizando
update_tabela(3000, 3000)
select_tabela()
select_tabela2()

#Deletando
delete_indice(7000)
select_tabela()
select_tabela2()


