import sqlite3

conexao = sqlite3.connect("jupyterNotebook/filmes.bd")
curs = conexao.cursor()

#Listando todo o banco
def selet_datebase():
    
    select_tabela = 'select * from filmes'
    curs.execute(select_tabela)
    dados_retorno = curs.fetchall()
    
    for i in dados_retorno:
        print(i)
        
selet_datebase()

#Atualizar um indice espeficico
'''def alterar_indice_banco():
    
    curs.execute("UPDATE filmes SET estudio = 'Platinum Dunes' WHERE nome = 'A Quiet Place: Part II'")
    conexao.commit()

alterar_indice_banco()'''

#Atualizar um indice espeficico recendo paramentros
a = "Platinum Dunes"
b = "A Quiet Place: Part II - test"
def alterar_indice_banco(alterar, nome_filme):

    query = "UPDATE filmes SET estudio = ? WHERE nome = ?"
    up = (alterar, nome_filme)
    curs.execute(query, up)
    conexao.commit()

alterar_indice_banco(a,b)
selet_datebase()

#Deletar via id
id_filme = 1
def deletar_filme( id_entrada ):

    query = "DELETE FROM filmes WHERE id = ?"
    dele = id_entrada
    curs.execute(query, (dele,))
    conexao.commit()
    
deletar_filme(id_filme)
selet_datebase()

#adicionando tudo novamente
def insert_datebase2(lista_filmes):
    
    insert_table = ("INSERT INTO filmes VALUES (?,?,?,?)")
    for i in lista_filmes:
        curs.execute(insert_table,i) 
    conexao.commit()

lista_filmes = [(4, 'Bond 25', 'Cary Fukunaga', 'Eon Productions, Metro-Goldwyn-Mayer'),
                (5, "Mulher Maravilha 1984", "Patty Jenkins", "‎Warner Bros. Pictures")]
insert_datebase2(lista_filmes)
selet_datebase()
curs.close()
conexao.close()



