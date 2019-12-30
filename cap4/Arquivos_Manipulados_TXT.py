text = "kono sekai wo uragitte \nhara no naka de ugometteiru \n"
text += "harawata kuiyabutte \nakaguroku minagitteiru"
print(text.upper())


#Criando um arquivo
import os
arquivo = open(os.path.join("arquivosUsados1/cientista.txt"),"w")


#Gravando no Arquivo separando a string via split() e fechando o arquivo com close()
for i in text.split():
    arquivo.write( i  + " ")
arquivo.close()


#Lendo o arquivo recem gravado
arquivo = open("arquivosUsados1/cientista.txt","r")
arqu = arquivo.read()
print(arqu.upper())


#Usando a expressão With - ele já realizada o close() automaticamente
with open("arquivosUsados1/cientista.txt","r") as arquivo:
    saida = arquivo.read()
print(len(saida))
print(saida)


#Lendo um arquivo entre diferentes partes
with open("arquivosUsados1/cientista.txt","w") as arquivo:
    arquivo.write(text[:22])
    arquivo.write("\n" + "\n")
    arquivo.write(text[:51])
    arquivo.write("\n" + "\n")
    arquivo.write(text[:72])
    arquivo.write("\n" + "\n")
    arquivo.write(text[:96])

with open("arquivosUsados1/cientista.txt","r") as arquivo:
    saida = arquivo.read()
print(saida)

