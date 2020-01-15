from pymongo import MongoClient
import datetime

#Abrindo conexao com o mongodb via a porta 27017
conexao = MongoClient("localhost", 27017)

#Instanciando o banco criando um banco chamado jogosdb
db = conexao.jogosdb
#colecoes é o mesm oque tabelas nos bancos relacionais
cole = db.jogosdb

#um banco Mongodb só é criado depois do primero insert
dicio_jogos = {"Id": "123","name_game": "God of War","year":"2018","date_register": datetime.datetime.utcnow()}
cole = db.ports
post_id = cole.insert_one(dicio_jogos)

dicio_jogos2 = {"Id": "124","name_game": "Devil My Cry 5","year":"2019","date_register": datetime.datetime.utcnow()}
cole = db.ports
post_id = cole.insert_one(dicio_jogos2)

#Retornando os dados inseridos
for post in cole.find():
    print(post)

print(db.name)
print(db.collection_names())

