import numpy as np
import matplotlib.pyplot as plt
import os

#np.__version__
help(np.array)

# Arraycriado apartir de uma lista
# podem ser, int, float, boolean, operações de numeros complexos e etc...
array = np.array([1.5,2.2,3.4,4.8,5.7,6.9,7.2,8.0,9.1])
print(array, "\n")

# np.concatenate((array_alt, array_alt2), axis=0) -> uni 2 arrays
array_alt = np.array([1,3,5,7])
array_alt2 = np.array([2,4,6,8])
print(np.concatenate((array_alt, array_alt2), axis=0), "\n")

# np.copy(array_alt2) -> copia uma array
array_alt3 = np.copy(array)
print(array_alt3, "\n")

# cumsum() -> func soma acumulada
print(array.cumsum(), "\n")

# shape -> Retorna a size da array
print(array.shape, "\n")

# np.around(array) -> Retorna um array com os valores arredondados
array_b = np.around(array)
print(array_b, "\n")

# array_c = array_b.flatten() -> copia uma array existente
array_c = array_b.flatten()
print(array_c, "\n")

# np.repeat(array_c, 3) -> retorna a repeticao de elementos em ordem crecente
print(np.repeat(array_c, 3), "\n")

# np.title(array_c, 3) -> retorna a repeticao de elementos em ordem de aparicao
print(np.tile(array_c, 3), "\n")

# np.arange(0,10,1) -> cria uma array de elementos de 0 a 9 
array_dois = np.arange(0,10,1)
print(array_dois, "\n")

print(array_dois.shape, "\n")

array_tres = np.arange(0,10,0.25)
print(array_tres, "\n")

# zeros(10), ones(10) e etc... -> cria uma matriz com elementos com unico tipo de numeto
# vai ser util nem Machine learn e deep learn
print(np.zeros(10), "\n")
print(np.ones(10), "\n")
print(np.ones((2,2)), "\n")

# np.eye("qualquer numero desejado") -> Cria uma matriz principal
array_quatro = np.eye(10)
print(array_quatro, "\n")

# Cria uma matriz principal recebedo um array de entrada
array_cinco = np.diag(np.array([1,2,3,4]))
print(array_cinco, "\n")

# criando uma matrix
array_cinco_partII = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(array_cinco_partII, "\n")

# max -> Retorna o maior valor do array
print(np.max(array_cinco_partII), "\n")
# min -> Retorna o menor valor do array
print(np.min(array_cinco_partII), "\n")

# Criando 2 arrays bidimensional com valores randomicos
# np.array_equal -> Comparando os elementos dos 2 arrays, para ver se sao iguais
array_cinco_partIII = np.diag(np.random.randn(250,2))
array_cinco_partIV = np.diag(np.random.randn(250,2))
print(np.array_equal(array_cinco_partIII, array_cinco_partIV), "\n")

#Matriz 3 por 3
matriz_um = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz_um, "\n")
#descricao da matriz
print(matriz_um.shape, "\n")

#criando uma matriz por np.matriz recebendo uma lista, tb pode receber uma tupla
lista_aux = [[10,58,57],[25,34,69],[80,42,21]]
matriz_dois = np.matrix(lista_aux)
print(matriz_dois, "\n")

# itemsize -> retorna o tamanho gasto na memoria por cada item
print(matriz_dois.itemsize, "\n")

# nbytes -> retorna o tamanho gasto na memoria por todos os elementos
print(matriz_dois.nbytes, "\n")

# Imprimindo um elememento recebendo uma coordenada da matriz
print(matriz_dois[1,1], "\n")

# Imprimindo um elememento recebendo uma coordenada da matriz
matriz_dois[1,1] = 31
print(matriz_dois, "\n")

# np pega o tipo da entrada, mas np decida o tipo que vai ser
# mas é possivivel alterrar o tipo para um desejado, -> dtype = np.float64 ou -> dtype = np.int32
w = np.array([1,2])
x = np.array([1.0,2.0])
y = np.array([1.0,2.0], dtype = np.int32)
z = np.array([1,2], dtype = np.float64)
print(w.dtype, x.dtype, y.dtype, z.dtype, "\n")

#tb é possivel fazer a mudança no momento da criacao da matriz
matriz_tres = np.array([[1,2,3,4],[5,6,7,8]], dtype = float)
print(matriz_tres, "\n")

print(np.linspace(0,10), "\n")

print(np.linspace(0,10,15), "\n")

print(np.logspace(0,5,10), "\n")

print(np.random.rand(10))

# Usando o matplotlib para fazer uma visualizacao com valores randomicos
plt.show((plt.hist(np.random.rand(1000))))

# visualizacao com valores randomicos com base na distribuicao dos valores
plt.show((plt.hist(np.random.randn(1000))))

imagem = np.random.rand(30,30)
plt.imshow(imagem, cmap = plt.cm.hot)
plt.colorbar()
print("\n")

nome = os.path.join("arquivos/iris.csv")
# !more Windows, Linux ou Mac !Head, ambos so funcionam no Jupyter
# get_ipython().system('more iris.csv')
leitura = np.loadtxt(nome, delimiter = ",", usecols = [0,1,2,3], skiprows = 1)
print(leitura, "\n")

leitura_uma, leittura_dois = np.loadtxt(nome, delimiter = ",", usecols = [0,1], skiprows = 1, unpack = True)
plt.show(plt.plot(leitura_uma, leittura_dois, "o", markersize = 8, alpha = 0.75))

array_aux = np.array([10,52,67,41])
# np.mean(array) -> Media dos valores do array
print(np.mean(array_aux), "\n")

# np.std(array) -> Desvio padrao dos valores do array
print(np.std(array_aux), "\n")

# np.var(array) -> variancia dos valores do array
print(np.var(array_aux), "\n")

# np.sum(array) -> soma dos elementos dentro do array
array_aux2 = np.arange(1,10)
print(np.sum(array_aux2), "\n")

# np.cumsum(array) -> soma acumulada dos elementos dentro do array
print(np.cumsum(array_aux2), "\n")

# np.prod(array) -> retorna o produto dos  elementos dentro do array
print(np.prod(array_aux2), "\n")

# Criando um array randomico de 2 elementos coordenados, depois fazer dua media
# criando um grafico no fim
array_aux3 = np.random.randn(250,2)
media_array = array_aux3.mean(0)
print(array_aux3, media_array, "\n")

plt.plot(array_aux3[:,0], array_aux3[:,1], "o", markersize = 5, alpha = 0.60)
plt.plot(media_array[0], media_array[1], "ro", markersize = 10)
print(plt.show(), "\n")
