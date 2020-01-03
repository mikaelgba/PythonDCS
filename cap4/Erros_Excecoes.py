#Forçando um erro
try:
    8 + "8"
          
except TypeError:
    print("Erro occorrido")
print("\n")
        

# In[ ]:
#Testando a estrutura com a gravação de um arquivo .txt
try:
    arquivo = open("arquivosUsados1/testandoerros.txt","w")
    arquivo.write("Gravando")
except IOError:
    print("Erro")
else:
    print("Arquivo Gravado")
finally:
    print("Fim da execução")
    arquivo.close()
print("\n")    
    

# In[ ]:
# Testando a leitura sem erro
try:
    arquivo2 = open("arquivosUsados1/testandoerros.txt","r")
    leitura = arquivo2.read()
    print(leitura)
except IOError:
    print("Erro")
else:
    print("Arquivo Gravado")
finally:
    print("Fim da execução")
    arquivo.close()
print("\n")


# In[ ]:
# Testando a leitura sem erro, buscando para leitura um arquivo que não existe
try:
    arquivo3 = open("arquivosUsados1/testandoerros1.txt","r")
    leitura = arquivo3.read()
    print(arquivo3)
except IOError:
    print("Erro")
else:
    print("Arquivo Gravado")
finally:
    print("Fim da execução")
    arquivo.close()
print("\n")


# In[ ]:
# Testando com uma função
def converter_int( ):

    try:
        valor_entrada = int(input("Digite um numero: "))
    except:
        print("Não foi digitado um numero ou não foi digidado nada")
    else:
        print("Numero valido: ", valor_entrada )

print(converter_int())
print("\n")


# In[ ]:
# Testando com uma função com loop interno que só finaliza quando digitado um numero
def converter_int2( ):
    
    '''Forma 1'''
    '''sair = True
    while (sair):
        
        try:
            valor_entrada = int(input("Digite um numero: "))
        except:
            print("Não foi digitado um numero ou não foi digidado nada")
        else:
            print("Numero valido:", valor_entrada )
            sair = False'''
 
    '''Forma 2'''
    while True:
        
        try:
            valor_entrada = int(input("Digite um numero: "))
        except:
            print("Não foi digitado um numero ou não foi digidado nada")
            continue
        else:
            print("Numero valido:", valor_entrada )
            break
            
print(converter_int2())
print("\n")


# In[ ]:
#Testando forçando um erro: adicionando um elemento na tupla. como não impossivel, então lança uma execeção
tupla = (1,2,3,4,5,6)

try:
    tupla.append(7)
    for i in tupla:
        print(i)
        3
except AttributeError as e:
    print("Erro:",e)
    
except IOError as e:
    print("Erro:",e)
    

