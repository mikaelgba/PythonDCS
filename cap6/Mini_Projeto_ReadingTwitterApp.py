#Pacotes do tweepy, datetime e json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from pymongo import MongoClient
import pandas as pd
import json
import sys

# uma tabela de conversão para mapear tudo fora do BMP
# encontrei a solucao no link abaixo
# https://stackoverflow.com/questions/32442608/ucs-2-codec-cant-encode-characters-in-position-1050-1050
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#chaves de acesso com o twitter
#Por motivos obvios de segurança da minha conta, Não irei colocar a as minhas chaves,Coleque as suas chaves de conexao"
consumer_key = "XXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#Criando o objeto de auteticar
auth = OAuthHandler(consumer_key, consumer_secret)
#Definir a autentificacao
auth.set_access_token(access_token, access_token_secret)

#Classe para pegar os dados do twitter via stream para salvar no MongoDB
class MyListenerTwitter( StreamListener ):
    
    def on_data( self, dados_twitter ):
        
        tweet = json.loads( dados_twitter )
        
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        object_twitter = {"created_at":created_at,
                          "id_str":id_str,
                          "text":text,}
        
        tweetind = col.insert_one(object_twitter).inserted_id
        print(object_twitter)
        return True


#Criando objeto mylistener
mylistener = MyListenerTwitter()
#Criando objeto mystream
mystream = Stream(auth, listener = mylistener)

#Conexão ao MongoDB
client = MongoClient('localhost', 27017)
#Criando o banco twitterdb
db = client.twitterdb
#Criando collection "col"
col = db.tweets2 

#Lista de palavras chaves a serem pesquisadas
keys_words = ["HQ","Games","Movie","E-Sports"]

#Buscando no Twitter tweets quem tenham as keyswords
mystream.filter(track=keys_words)

mystream.disconnect()
col.find_one()

for t in db.tweets2.find():
    print(t["created_at"],"\n",t["id_str"],"\n")
    print(t["text"].translate(non_bmp_map),"\n")

dados_banco = [{"created_at": i["created_at"],
                "text": i["text"].translate(non_bmp_map),} for i in col.find()]

#Criando e imprimindo dataframe
df = pd.DataFrame(dados_banco)
print(df)
