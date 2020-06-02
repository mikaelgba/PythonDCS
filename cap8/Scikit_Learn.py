import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn
from sklearn.linear_model import LinearRegression # Algaritmo de treino
from sklearn.model_selection import train_test_split # algaritmo de teste
from sklearn.datasets import load_boston # dataset da biblioteca
from IPython.display import Image

Image('arquivos/ml_map.png')

# Aplicacao simples de machine learn - prevendo preço de uma pizza de acordo com seu diametro
diametro, preco = [[7],[10],[15],[30],[45]], [[8],[11],[16],[38.5],[52]]

plt.figure()
plt.figsize = (12,6)
plt.scatter(diametro, preco, label = "Preço sobre diametro", color = "r")
plt.grid(True)
plt.axis([0, 60, 0, 60])
plt.xlabel("Diametro da Pizza")
plt.ylabel("Preço")
plt.show()

# invocando o algaritomo de apredizagem
model = LinearRegression()

# passando os dados para a apredizagem
model.fit(diametro, preco)

for i in range(10,101,10):
    print("Uma Pizza de", i, "cm tem o custo de: %.2f" % model.predict([[i]]),"!")

plt.figure()
plt.figsize = (12,6)
plt.scatter(diametro, preco, color = "g")
plt.plot(diametro, model.predict(diametro))
plt.grid(True)
plt.show()


# Aplicacao com o dataset da biblioteca do sklearn.datasets
boston = load_boston()
print(boston.data.shape, 
      "\n", boston.DESCR,
      "\n", boston.feature_names)


dataframe = pd.DataFrame(boston.data)
print(dataframe.head(10), "\n")

dataframe.columns = boston.feature_names
print(dataframe.head(10), "\n")

print(boston.target)

dataframe["PRICE"] = boston.target
print(dataframe.head(10), "\n")


datas_learn = dataframe.drop("PRICE", axis = 1)
price_house = dataframe.PRICE

plt.figure()
plt.figsize = (12,6)
plt.scatter(dataframe.RM, price_house, color = "g")
plt.grid(True)
plt.show()

# Treinando
model_house = LinearRegression()
model_house.fit(datas_learn, price_house)


print("Coeficiente: ", model_house.intercept_,
      "\n", "Nº de Coeficientes : ", len(model_house.coef_))


model_house.predict(datas_learn)

plt.figure()
plt.figsize = (12,6)
plt.scatter(dataframe.PRICE, model_house.predict(datas_learn), color = "y")
plt.xlabel("Preço Original")
plt.ylabel("Preço Previsto")
plt.grid(True)
plt.show()

# Da maneira que foi realizada não é aconselhavel 
# pois os dados foram testados com os mesmos do treinamento
# o recomendado é fazer atraves de separação  do que é "TREINO" e "TESTE"
# e o mais ideial ainda é fazer essa divisão de forma randomica
# Assim não havera interferência de terceiros

# Divisão dos dados do dataset entre o que é TREINO E TESTE pré treino
datas_learn_train, datas_learn_test, price_house_train, price_house_test = train_test_split(datas_learn, 
                                                                                            dataframe.PRICE, 
                                                                                            test_size = 0.30, 
                                                                                            random_state = 5)
print(datas_learn_train.shape, "\n", 
      datas_learn_test.shape, "\n", 
      price_house_train.shape, "\n", 
      price_house_test.shape, "\n")

# Treinando
new_model_house = LinearRegression()
new_model_house.fit(datas_learn_train, price_house_train)

# separeção dos dados do treino e teste para a visualição
treino = new_model_house.predict(datas_learn_train)
test = new_model_house.predict(datas_learn_test)

print("Coeficiente: ", new_model_house.intercept_,
      "\n", "Nº de Coeficientes : ", len(new_model_house.coef_))


plt.figure()
plt.figsize = (12,6)
plt.title("Resultado do plot: Treino(Vermelho) e Teste(Azul)")

plt.scatter(price_house_test, 
            new_model_house.predict(datas_learn_test), 
            color = "b", s = 40, alpha = 0.5)
plt.show()


# Visualisação para compraração 
plt.figure()
plt.figsize = (12,6)
plt.title("Resultado do plot: Treino(Vermelho) e Teste(Azul)")

plt.scatter(new_model_house.predict(datas_learn_train), 
            new_model_house.predict(datas_learn_train) - price_house_train, 
            color = "r", s = 40, alpha = 0.5)
plt.scatter(new_model_house.predict(datas_learn_test), 
            new_model_house.predict(datas_learn_test) - price_house_test, 
            color = "b", s = 40, alpha = 0.5)

plt.hlines(y = 0, xmin = 0, xmax = 50)
plt.show()
