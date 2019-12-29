def soma(a,b): return a + b

def subt(a,b): return a - b

def mult(a,b): return a * b

def divi(a,b): return a / b

while(True):
    
    print("Python Calc",
          "\n","Opções:", 
          "\n", "1 - Soma", 
          "\n", "2 - Subtração",
          "\n", "3 - Multiplicação",
          "\n", "4 - Divisão", "\n")
    
    tipo = int(input("Qual tipo ode operação: 1, 2, 3 ou 4? \n"))
    valor1 = float(input("Digite o primeiro valor: \n"))
    valor2 = float(input("Digite o segundo valor: \n"))
    
    if (tipo == 1):
        #retorna um print da soma
        print(valor1, "+", valor2,"=",soma(valor1,valor2), "\n")
        
    elif(tipo == 2):
        #retorna um print da subtração
        print(valor1, "-", valor2,"=",subt(valor1,valor2), "\n")
        
    elif(tipo == 3):
        #retorna um print da multiplicação
        print(valor1, "*", valor2,"=",mult(valor1,valor2), "\n")
        
    elif(tipo == 4):
        #retorna um print da divisão
        print(valor1, "/", valor2,"=",divi(valor1,valor2), "\n")
        
    else:
        print("Opção invalida! \n")

