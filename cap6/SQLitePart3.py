import sqlite3
conexao = sqlite3.connect("jupyterNotebook/filmes.bd")
cursorC = conexao.cursor()

#Listando todo o banco
def selet_datebase():
    
    select_tabela = 'select * from filmes'
    cursorC.execute(select_tabela)
    dados_retorno = cursorC.fetchall()
    
    for i in dados_retorno:
        print(i)
        
selet_datebase()

#Listando linha(as) especificas
def selet_datebase2_linhas():
    
    select_tabela = 'select * from filmes where id > 2'
    cursorC.execute(select_tabela)
    dados_retorno = cursorC.fetchall()
    
    for i in dados_retorno:
        print(i)
        
selet_datebase2_linhas()

#Listando Coluna(as) especificas
def selet_datebase3_colunas():
    
    select_tabela = 'select * from filmes'
    cursorC.execute(select_tabela)
    dados_retorno = cursorC.fetchall()
    
    for i in dados_retorno:
        print(i[1])
        
selet_datebase3_colunas()

cursorC.close()
conexao.close()



