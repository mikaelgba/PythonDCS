#Importando pacote Math
import math
dir(math)


#Ultilixando a metodo sqrt() que retona a raiz quadrada do valor de entrada
print(math.sqrt(25))


#Importando somente o metodo sqrt()
from math import sqrt
print(sqrt(25))


#Importando pacote random e ultilizando metodo choice() para selecionar um elemento da lista 
import random
lista = ["a","b","c"]
print(random.choice(lista))


#Ultilixando a metodo sample() que retorna valores randomicos com base no tamanho maixmo - range(100); mais 10 - que listar10 valores
random.sample(range(100),10)


#Importando pacote statistics para aplicações estatisticas 
import statistics
lista2 = [5,7.2,8,7,6.4,6]
#mean() retorna a media
print(statistics.mean(lista2))
#median() retorna a mediana
print(statistics.median(lista2))

#print(statistics.median(lista2))


#Importando pacote os para aplicações de sistemo operacinais
import os
#retona o diretorio 
print(os.getcwd())


#Importando pacote que também para aplicações de sistemo operacinais
import sys
print(sys.stdout.write("Comunismo não funciona"))


#retona a versão do interpretador
print(sys.version)


#Importando pacote com aplicações WEB
import urllib.request
#abrer conexão com um link desejado
link = urllib.request.urlopen("http://python.org")
print(link)
print(link.read())





