import os
os.remove("jupyterNotebook/filme.db") if os.path.exists("jupyterNotebook/filmes.db") else None

import sqlite3
conex = sqlite3.connect("jupyterNotebook/filmes.bd")
cur2 = conex.cursor()

def create_tabela():
    cur2.execute('CREATE TABLE IF NOT EXISTS filmes(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, diretor TEXT, estudio TEXT)')

def insert_datebase():
    cur2.execute("INSERT INTO filmes VALUES (1, 'Bond 25', 'Cary Fukunaga', 'Eon Productions, Metro-Goldwyn-Mayer')")
    conex.commit()
    cur2.close()
    conex.close()

create_tabela()
insert_datebase()

#Recuperando os dados
conex2 = sqlite3.connect("jupyterNotebook/filmes.bd")
cur3 = conex2.cursor()
select_tabela = 'select * from filmes'
cur3.execute(select_tabela)
dados_retorno = cur3.fetchall()

for i in dados_retorno:
    print(i)
    
cur3.close()
conex2.close()

#Alterando a func insert_datebase() para receber paramentros de entrada
def insert_datebase2(lista_filmes):
    
    insert_table = ("INSERT INTO filmes VALUES (?,?,?,?)")
    for i in lista_filmes:
        cur4.execute(insert_table,i)
        
    conex3.commit()
    cur4.close()
    conex3.close()

filmes = [(2, "A Quiet Place: Part II", "John Krasinski", "‎Platinum Dunes"),
        (3,"Kingsman: O Grande Jogo","Matthew Vaughn","Fox")]

conex3 = sqlite3.connect("jupyterNotebook/filmes.bd")
cur4 = conex3.cursor()

insert_datebase2(filmes)

#listar banco
def selet_datebase():
    
    select_tabela = 'select * from filmes'
    cur5.execute(select_tabela)
    dados_retorno = cur5.fetchall()
    
    for i in dados_retorno:
        print(i)

    conex4.commit()
    cur5.close()
    conex4.close()

conex4 = sqlite3.connect("jupyterNotebook/filmes.bd")
cur5 = conex4.cursor()
selet_datebase()
    



