#1
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

foguete = Rocket(2,5)
print(foguete.print_rocket(),"\n")
foguete.move_rocket(5,7)
print(foguete.print_rocket(),"\n")

#2
class Pessoa():

    def __init__( self, nome, cidade, telefone, email ):

        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        
    #Nome
    def getNome( self ):
        return self.nome

    def setNome( self, novo_nome ):
        self.nome = novo_nome
        
    #cidade
    def getCidade( self ):
        return self.cidade

    def setCidade( self, nova_cidade ):
        self.cidade = nova_cidade
        
    #telefone
    def getTelefone( self ):
        return self.telefone

    def setTelefone( self, novo_telefone ):
        self.telefone = novo_telefone
        
    #email
    def getEmail( self ):
        return self.email

    def setEmail( self, novo_email ):
        self.email = novo_email

pess = Pessoa("Michael", "Guarabira", "987654321", "mikaelgba@gmail.com")
print(pess.getNome(),"\n")
print(pess.getCidade(),"\n")
print(pess.getTelefone(),"\n")
print(pess.getEmail(),"\n")

#3
class Smartphone():

    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

    #tamanho
    def getTamanho( self ):
        return self.tamanho

    def setTamanho( self, novo_tamanho ):
        self.tamanho = novo_tamanho

    #interface
    def getInterface( self ):
        return self.tamanho

    def setInterface( self, nova_interface ):
        self.interface = nova_interface

class Mp3Player( Smartphone ):

    def __init__( self, tamanho, interface, capacidade ):
        
        Smartphone.__init__(self, tamanho, interface)
        self.capacidade = capacidade

    #Capacidade limite
    def getCapacidade( self ):
        return self.capacidade

    def setCapacidade( self, nova_capacidade):
        self.capacidade = nova_capacidade

    def info_Mp3( self ):
        return "Mp3Player de tamanho %d com interface %s e capacidade %d" %(self.tamanho, self.interface, self.capacidade)

mp3 = Mp3Player(15, "LED", 64)
print(mp3.info_Mp3(),"\n")
print(mp3.getTamanho(),"\n")
print(mp3.getInterface(),"\n")
print(mp3.getCapacidade())

