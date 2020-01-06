#Super-classe Animal
class Animal ():
    
    def __init__( self ):
        print("Novo animal")
    
    def ident ( self ):
        print("Animal")
        
    def comer( self ):
        print("comendo")

#Sub-classe Mamimefero da Super-classe Animal
#o atributo sub_class_animal é o tipo de sub classe animal dentro entre os mamiferos como visto no link abaixo
#https://escolakids.uol.com.br/ciencias/classificacao-dos-mamiferos.htm
class Mamifero( Animal ):

    def __init__ ( self, sub_animal ):
        self.sub_animal = sub_animal
        print("Novo mamifero")
        
    def ident ( self ):
        print("Mamifero")

    def getSub_animal( self ):
         return sub_animal
        
    def setSub_animal( self, nova_sub_animal ):
        sub_animal = nova_sub_animal

#Sub-classe Cachorro da Sub-classe Mamimefero da Super-classe Animal
class Cachorro( Mamifero ):

    def __init__( self, sub_animal, raca, tamanho, idade ):
        
        self.sub_animal = sub_animal
        self.raca = raca
        self.tamanho = tamanho
        self.idade = idade    

    # %.2f limita para apenas 2 casas decimais  
    def ident ( self ):
        print("Sub-Classe animal: %s - Cachorro de raça: %s - de tamanho %.2f - e com idade de %d anos"
              %(self.sub_animal, self.raca, self.tamanho, self.idade))

    def getRaca( self ):
        return self.raca
    
    def setRaca( self, nova_raca ):
        self.raca = nova_raca
        
    def getTamanho( self ):
        return self.tamanho
    
    def setTamanho( self, novo_tamanho ):
        self.tamanho = novo_tamanho
        
    def getIdade( self ):
        return self.idade
    
    def setIdade( self, nova_idade ):
        self.idade = nova_idade


# In[ ]:
anim = Animal()
anim.comer()
anim.ident()

# In[ ]:
mami = Mamifero("Prototheria")
mami.comer()
mami.ident()

# In[ ]:
cao = Cachorro("XXX", "Pastor Alemão", 1.50, 5)
cao.comer()
cao.ident()





