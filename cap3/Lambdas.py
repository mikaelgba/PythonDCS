def potencia(entrada):
    saida = entrada**2
    return saida
print(potencia(5))

#Refatorando a função
def potencia(entrada):
    return entrada**2
print(potencia(5))

#Refatorando a função
def potencia(entrada): return entrada**2
print(potencia(5))

#Exemplo de aplicação de uma Lambda - Lambda é uma função simples
potencia2 = lambda entra: entra**2
print(potencia2(5))

#Exemplo de aplicação de uma Lambda com condicional logica
boole = lambda entrada: entrada % 2 == 0
print(boole(5))
print(boole(4))

nome = lambda nom: nom[0]
print(nome("Foo Fighters"))

rever = lambda revers: revers[::-1]
print(rever("Foo Fighters"))

#Exemplo de aplicação de uma Lambda com mais de um parametro
soma = lambda a,b: a + b
print(soma(7,8))

