class Circulo():
    
    # pi é um varialvel global da classe
    pi = 3.14
    # com raio = 'x valor' toda vez que criar um objeto Circulo ele automaticamnete já concidera que o raio será 'x valor' 
    #mas se colocar um outro valor ele vai sobreescrever o 'x valor'
    def __init__( self, raio = 3 ):        
        self.raio = raio
        
    def area( self ):
        return ((self.raio * self.raio) * Circulo.pi)
    
    def getRaio( self ):
        return self.raio
    
    def setRaio( self, novo_circulo ):
        self.raio = novo_circulo

circulo = Circulo(4)

print(circulo.getRaio(),"\n")

print(circulo.area(),"\n")

circulo.setRaio(7)

print(circulo.area(),"\n")


#Classe quadrado
class Quadrado():

    def __init__( self, altura, largura ):
         self.altura = altura
         self.largura = largura

    def area( self ):
        return ( self.altura * self.largura )

    def getAltura( self ):
        return self.altura

    def setAltura( self, nova_altura ):
        self.altura = nova_altura

    def getLargura( self ):
        return self.largura

    def setLargura( self, nova_largura ):
        self.largura = nova_largura
  
quad = Quadrado(2,2)

print("Altura:",quad.getAltura(),"Largura:", quad.getLargura(),"\n")

print(quad.area(),"\n")

quad.setAltura(4)

print(quad.getAltura(),"\n")

quad.setLargura(4)

print(quad.getLargura(),"\n")

print(quad.area(),"\n")

