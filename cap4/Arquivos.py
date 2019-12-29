#Abrindo elendo um o primeiro aquivo
arquivo = open("arquivosUsados1/arquivo1.txt","r")
print(arquivo.read())

arquivo = open("arquivosUsados1/arquivo1.txt","r")
print(arquivo.read(10))

#Conta a quantidade de caracteres tem no arquivo aberto
print(arquivo.tell())

#Começa a leitura apartir de um uma ponto desejado como entrada
print(arquivo.seek(0,0))
arquivo.close()

#Escrita no arquivo aberto - "w" sobreescreve o arquivo
arquivo = open("arquivosUsados1/arquivo1.txt","w")
arquivo.write("- My chemical Romance")
arquivo.close()
arquivo = open("arquivosUsados1/arquivo1.txt","r")
print(arquivo.read())
arquivo.close()

#Escrita no arquivo aberto - "a" adiciona no arquivo sem sobrecrever
arquivo2 = open("arquivosUsados1/arquivo2.txt","a")
arquivo2.write("- Voltando")
arquivo2.close()
arquivo2 = open("arquivosUsados1/arquivo2.txt","r")
print(arquivo2.read())
arquivo2.close()




