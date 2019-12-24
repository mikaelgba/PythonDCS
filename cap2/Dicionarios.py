dicio1 = {"Mu":1,"Aiolia":5,"Aiolos":9,"Aldebaran":2,"Shaka":6,"Shura":10,"Saga":3,"Dorko":7,"Kamus":11,"Mascará da Morte":4,"Miro":8,"Afodite":12}
print(dicio1)

print(dicio1["Mu"])

#Limpar os elementos do Dicionario
dicio1.clear()
print(dicio1)

dicio2 ={"Seiya":13,"Shiryu":15,"Ikki":15,"Yoga":14,"Shun":13}
dicio2["Seiya"] = 14
print(dicio2)

#Retorna se há uma chave no dicionario
print("Seiya" in dicio2)

#Retorna se há uma elemento no dicionario
print(13 in dicio2.values())

#Retorna o tamanho
print(len(dicio2))

#Retorna as chaves dos elementos
print(dicio2.keys())

#Retorna os elementos do dicionario
print(dicio2.values())

#Retorna os elementos do dicionario
print(dicio2.items())

#Mescla 2 dicionarios
dicio3 = {"Saori":14, "Karno":23}
dicio2.update(dicio3)
print(dicio3)

dicio4 = {1:"eu", 2:"você",3:"e o zubumafu"}
print(dicio4[1].upper())

dicio4 = {1:"eu", 2:"você",3:"e o zubumafu"}
print(dicio4[1].lower())

#Adicionando um elemento
dicio4[4] = " para sempre"
print(dicio4)

#Removendo um elemento
del dicio4[4]
print(dicio4)

#Dicioario com subListas
dicio5 = {"a":[23,58,19],"b":[35,75,95],"c":[41,53,24]}
dicio5["a"][0] -= 2
print(dicio5)

#Dicioario com mais de uma chave para cada elemento
dicio6 = {"id1":{"user1":"a"},"id2":{"user2":"b"}}
dicio6["id1"]["user1"] = "A"
dicio6["id2"]["user2"] = "B"
print(dicio6)


