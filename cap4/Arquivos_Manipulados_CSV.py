#importando o modulo csv - "excel"
import csv

#Escrevendo o arquivo csv
with open('arquivosUsados1/numeros.csv','w') as arquivo:
    escrita = csv.writer(arquivo)
    escrita.writerow(["a","b","c"])
    escrita.writerow([10,20,30])
    escrita.writerow([40,50,60])


#Lendo o arquivo csv
with open('arquivosUsados1/numeros.csv','r') as arquivo:
    leitura = csv.reader(arquivo)
    for i in leitura:
        if(i != []):
            print(len(i))
            print(i)


#Lendo as celulas separadas
with open("arquivosUsados1/numeros.csv","r") as arquivo:
    leitura = csv.reader(arquivo)
    saida = list(leitura)
print(saida)


for i in saida[1:]:
    print(i)

