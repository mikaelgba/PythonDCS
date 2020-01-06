#Classe Livro
#Metodos especiais são metodos dentro da classe do objeto que permitem trabalhar o objeto com diversas funções Buiit-in
class Livro ():
    
    def __init__( self, nome, autor, paginas ):
        
        self.nome = nome
        self.autor = autor
        self.paginas = paginas
        
    #Metodo que faz o mesmo serviço que print(livr)
    #Mas deixando claro, se já existe metodos que fazem a mesma coisa.
    #então não é necessario criar uma dentro da classe
    def __str__( self ):
        return "Nome: %s - Autor: %s - Paginas: %d" %(self.nome, self.autor, self.paginas)

    def getNome( self ):
        return self.nome

    def setNome( self, novo_nome ):
        self.nome = novo_nome
    
    def getAutor( self ):
        return self.autor
    
    def setAutor( self, novo_autor ):
        self.autor = novo_autor
    
    def getPaginas( self ):
        return self.paginas

    def setPaginas( self, novas_paginas ):
        self.paginas = novas_paginas
    
        
# In[ ]:
livr = Livro("O Senhor do Anéis, O retorno do rei", "J. R. R. Tolkien", 380)
print(str(livr),"\n")
print(livr.getAutor(),"\n")

# In[ ]:
print(livr,"\n")

# In[ ]:
del livr.paginas

# In[ ]:
print(hasattr(livr, "paginas"),"\n")
livr.setPaginas(380)
print(livr.getPaginas())




