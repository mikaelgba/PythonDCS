#Criar Funções
#Função sem paramentro de entrada
def printAux():
    print("Look Alive, Sunshine")
printAux()

#Função com paramentro de entrada
def printAux2(entrada):
    print("Look Alive, Sunshine -", entrada)
printAux2("My Chemical Romance")

def multiplicacao(valor):
    for i in range(10):
        print(valor, "X", i + 1, "=",valor * i + 1)
multiplicacao(5)      

#Função com dois paramentros de entrada
def divicao(valor1, valor2):
    print(valor1, "/", valor2, "=", valor1 / valor2)
divicao(10,2)

#Funções Buiit-in
#Função - abs("numero") - retorna o valor absoluto ex: entrada: -15, saisa: 50
print(abs(-50))

#Função - bool() - retorna o valor booleano
print(bool(0))
print(bool(1))

#Funções Str, Float e Int
#Função int() - numeros inteiros
numero = int(input("Numero: "))
if(numero % 2 == 0):
    print("par")
else:
    print("impar")

print(int("5"))

#Função float() - numeros flutuantes
print(float("5"))
print(float("85.5"))

#Função str() - transforma em um String
print(str("cinco"))
print(str.lower("cinco"))
print(str.upper("cinco"))

#Função len(x) - retorna o tamanho de uma entrada 'X' desejada
a = [1,2,3,4]
print(len(a))
print(len("Seiya"))

#Função max(x) - retorna o maior elemento de uma entrada 'X' desejada
print(max(a))

#Função min(x) - retorna o menor elemento de uma entrada 'X' desejada
print(min(a))

#Função min(x) - retorna a soma de todos os valores
print(sum(a))

#Importando a biblioteca math, para usar a função math.sqrt() que faz a raiz quadrada de uma entrada 'x'
import math

def numeroPrimo(entrada):
    if((entrada % 2 == 0) and (entrada > 2)):
        return("Não é numero primo")
    for i in range(3, int(math.sqrt(entrada)) + 1, 2):
        if(entrada % i == 0):
            return("não é primo")
    return("é primo")
print(numeroPrimo(23))

#Função split() retorna a String separadas pelos seus indices nulos
def splitString(entrada):
    return entrada.split()
print(splitString("Faça elevar, o cosmo em seu coração!"))
var = splitString("Faça elevar, o cosmo em seu coração!")
print(var)

# *vartuple permite ter um ou diversas entrdas de paramentos
def relatar(entrada , *vartuple):
    print("Entrada foi:", entrada)
    
    for i in vartuple:
        print("Entrada foi:", i)
    return;
relatar("The Kids From Yesterday")
relatar("a","b","c")
