#Criando a classe carro
class Carro():
    
    def __init__( self, nome, modelo, chasi ):
        self.nome = nome
        self.modelo = modelo
        self.chasi = chasi
        
    def definicao( self ):
        return self.nome, self.modelo,self.chasi     


# In[ ]:
#Adicionando elementos e lendo
carros = []
letr = "ABCDEF"

for i in range(len(letr)):
    
    a = Carro(letr[i], letr[i], i)
    carros.append(a)
    
for j in range(len(carros)):
    print(carros[j].definicao())
print()

# In[ ]:
#Cruiando classe Funcionario
class Funcionario():
    
    def __init__( self, nome, cargo, salario ):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def descricao_func( self ):
        return "Funncioario: %s \nCargo: %s \nSalario: %d" %(self.nome, self.cargo, self.salario)


# In[ ]:
funcio1 = Funcionario("Eu", "Dono", 10000)
print(funcio1.descricao_func())
print()


# In[ ]:
# hasattr() verifica se há um atributo
print(hasattr(funcio1,"nome"))
print()


# In[ ]:
# setattr() altera o atributo
print(setattr(funcio1, "salario", 10500))
print()


# In[ ]:
# getattr() obtem o atributo
print(getattr(funcio1, "salario"))
print()


# In[ ]:
# delattr() deleta o atributo
print(delattr(funcio1, "salario"))

