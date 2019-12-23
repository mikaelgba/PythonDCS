texto ="DC é melhor que a Marvel nas Hqs"

#ler até o indice 10
print(texto[:11])

#retorna o ultimo indice
print(texto[-1])

#retorna p 1 indice
print(texto[1])

#retorna a string com intervalos de 1 em 1
print(texto[::1])

#retorna a string com intervalos de 2 em 2
print(texto[::2])

#retorna a string com intervalos de 1 em 1 de trás para frente
print(texto[::-1])

#manipulção numerica com String
letra = "w"
print(letra * 3)

#maiúsculo
print(letra.upper())

#minúsculo
print(letra.lower())

#retorna a String dividia entre seus elementos não nulos
print(texto.split())

#retorna a String dividia por um elemento 'X' entrada
print(texto.split('m'))

#retorna o primeito elemento maiúsculo
print(texto.capitalize())

#retorna a quantidade de um elemento 'X' entrada
print(texto.count('a'))

#retorna o indice de um elemento 'X' entrada
print(texto.find("v"))

print(texto.islower())

print(texto.isspace())

print(texto.endswith("o"))




