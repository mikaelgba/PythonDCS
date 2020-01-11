# Criando um dicionario
dicio = {"Nome": "Yoda", "Serie": "The Madalorian", "Filme": ["Star Wars 1", "Star Wars 2", "Star Wars 3"]}
for i, j in dicio.items():
    print(i, j)
print("\n")

# Importando o JSON
import json

print(json.dumps(dicio))
print("\n")

# Criando um arquivo do tipo json
with open("arquivosUsados1/dados.json", "w") as arquivo:
    arquivo.write(json.dumps(dicio))

# Lendo o arquivo json recém criado
with open("arquivosUsados1/dados.json", "r") as arquivo:
    arqui_json = arquivo.read()
    saida = json.loads(arqui_json)
    print(saida)
print(saida["Nome"])
print("\n")

# Lendo um arquivo json na web
from urllib.request import urlopen

arquivo_web = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
saida2 = json.loads(arquivo_web)[0]
print('Título: ', saida2["title"])
print('URL: ', saida2["url"])
print("\n")

# Copiando um arquivo para outro
origem = "arquivosUsados1/dados.json"
destino = "arquivosUsados1/json_dados.txt"

# Opção 1:
with open(origem, "r") as arquivo1:
    text = arquivo1.read()
    with open(destino, "w") as arquivo2:
        arquivo2.write(text)

# Opção 2:
open(destino, "w").write(open(origem, "r").read())

# Lendo o arquivo json
with open("arquivosUsados1/json_dados.txt", "r") as lido_json:
    text3 = lido_json.read()
    imp = json.loads(text3)
print(imp)
print("\n")
