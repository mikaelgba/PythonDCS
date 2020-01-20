import pymongo

#Abrindo conexap om o banco
conexao = pymongo.MongoClient()
#conexao.database_names()
db = conexao.jogosdb
#db.collection_names()

#Criando o banco
db.create_collection("Empresas_jogos")
#db.collection_names()

#Criando os docs
empre1 = {"id": "111", "name":"Konami", "sede": ["Minato", "Tóquio"]}
empre2 = {"id": "112", "name":"Nintendo", "sede": ["Quioto", "Japão"]}
empre3 = {"id": "113", "name":"Square Enix", "sede": ["Shinjuku", "Tóquio"]}
empre4 = {"id": "114", "name":"Ubisoft", "sede": ["Montreuil"]}
empre5 = {"id": "115", "name":"Activision Blizzard", "sede": ["Santa Mônica - Califórnia"]}
empre6 = {"id": "116", "name":"Capcom", "sede": ["Osaka"]}

db.Empresas_jogos.insert_one(empre1)
db.Empresas_jogos.insert_one(empre2)
db.Empresas_jogos.insert_one(empre3)
db.Empresas_jogos.insert_one(empre4)
db.Empresas_jogos.insert_one(empre5)
db.Empresas_jogos.insert_one(empre6)

for empre in db.Empresas_jogos.find():
    print("Empresa")
    print(empre,"\n")
    
