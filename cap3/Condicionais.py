if( 3 < 5):
    print("Saint Seiya!!")

if( 10 == 5):
    print("true")
else:
    print("false")

if True:
    print("True")

#Condicionis Aninhadas
idade = 5
nome = "Yoda"
if(idade >= 5):
    if(nome == "Yoda"):
        print("Iti Malia, Baby Yoda!!")
else:
    print("Você não é o Baby Yoda")

#Condicional logico AND
idade = 5
nome = "Yoda"
if(idade >= 5) and (nome == "Yoda"):
    print("Iti Malia, Baby Yoda!!")
else:
    print("Você não é o Baby Yoda")

#Condicional logico OR
idade = 4
if(idade >= 5) or (nome == "Yoda"):
    print("Hum, talvez você não seja o Iti Malia, Baby Yoda!!")

#Condicional logico NOT
nome2 = "Yoda"
if not (nome2 == "Yoda"):
    print("Você não é o Baby Yoda")
else:
    print("Iti Malia, Baby Yoda!!")

#Condicinal Elif
cavaleiro = "Seiya"
if(cavaleiro == "Seiya"):
    print(cavaleiro, "O motador de Deuses")
elif(cavaleiro == "Hades"):
    print(cavaleiro, "Geral ai morrer!")
else:
    print("Quem eis você?")

# -----

filme_premiado = "Coringa"
oscar = 4

if(filme_premiado == "Coringa") and (oscar == 4):
    print(filme_premiado,"ganhou",oscar,"Oscars.")
else:
    print("Irlandês ganhou alguns também.")

#Usando mais de uma condicição no If
filme_premiado2 = input("Filme? ")
oscar2 = int(input("Quantidade de Oscars? "))

if(filme_premiado2 == "Coringa") and (oscar2 == 4):
    print(filme_premiado2,"ganhou",oscar2,"Oscars.")
else:
    print("Irlandês ganhou",oscar2)

#Usando três condicições no If
oscar_melhor_ator = input("Melhor ator? ")
filme_premiado2 = input("Filme? ")
oscar2 = int(input("Quantidade de Oscars? "))

if(filme_premiado2 == "Coringa") and (oscar2 == 4) and (oscar_melhor_ator == "Joaquin Phoenix"):
    print(filme_premiado2,"ganhou",oscar2,"Oscars, entre eles o de melhor ator para",oscar_melhor_ator)
else:
    print("Irlandês ganhou",oscar2)

# -----

valor = float(input("Valor? "))
quant = int(input("Quantidade? "))
desconto = input("Há desconto? ")

total = valor * quant

if(total >= 500) and (desconto == "sim"):
    total -= (total/25)
    print("Total = %r"%(total))
else:
    print("Total = %r"%(total))
    
