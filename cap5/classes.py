# Classe livro
class Livro():
    
    #__init__ é o metodo construtor da classe, ele que inicializa cada objeto estanciado pela classe Livro
    def __init__( self ):
        
        #self indica que o abritubdo pertence ao objeto Livro
        self.nome = "Narnia"
        self.isbn = 123456
        print("Class criada")
      
    # Métodos são funções que ganham parâmetros para os atributos do objeto
    def definicao( self ):
        return "livro %s com isbn %d" %(self.nome, self.isbn)


# In[ ]:
livro = Livro()

# In[ ]:
print(type(livro), "\n")


# In[ ]:
print(livro.definicao(), "\n")
print(livro.nome, "\n")


# In[ ]:
# Classe livro com parâmetros de entrada
class Livro2():
    
    #__init__ é o metodo construtor da classe, ele que inicializa cada objeto estanciado pela classe Livro
    def __init__( self, nome, isbn ):
        
        #self indica que o abritubdo pertence ao objeto Livro
        self.nome = nome
        self.isbn = isbn
        #print("Class criada")
      
    # Métodos são funções que ganham parâmetros para os atributos do objeto
    def definicao2( self ):
        return "livro %s com isbn %d" %(self.nome, self.isbn)


# In[ ]:
livro2 = Livro2("Senhor dos anéis", 1234567)
print(livro2.definicao2(), "\n")


# In[ ]:
class Cachorro():
    
    def __init__( self, raca, tamanho, idade ):
        
        self.raca = raca
        self.tamanho = tamanho
        self.idade = idade
        
    #%s - String / %d inteiro / %f - flutuante
    def definicao( self ):
        return "Raça %s de tamanho %d com idade %d" %(self.raca, self.tamanho, self.idade)


# In[ ]:
cao = Cachorro("Cão Brasileiro caramelo", 120, 5)


# In[ ]:
print(cao.definicao(), "\n")
print(cao.raca)

