contador = 0
while (contador < 10):
    contador += 1
print(contador)

#While loop Aninhado
contador2 = 0
while(contador2 < 10):
    contador3 = 0
    while(contador3 < 10):
        print(contador2 + 1, "X", contador2 + 1, "=", (contador2 + 1) * (contador2 + 1))
        contador3 += 1
    contador2 += 1

#PASS, BREAK E CONTINUE
#PASS: deixa continuando o loop
#BREAK: interrompe o loop
#CONTINUE: pula uma interação
contador4 = 0
while(contador4 < 10):
    if(contador4 == 6):
        break
    else:
        pass
    print(contador4)
    contador4 += 1

contador5 = "Programador"
i = 0
while(i < len(contador5)):
    if(contador5[i] == "m"):
        continue
    print(contador5[i])
    i += 1

