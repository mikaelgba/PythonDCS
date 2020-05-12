import numpy as np

#np.__version__
help(np.array)

#Arraycriado apartir de uma lista
#podem ser, int, float, boolean, operações de numeros complexos e etc...
array= np.array([1,2,3,4,5,6,7,8,9])
print(array, "\n")

#func soma acumulada
print(array.cumsum(), "\n")

#Retorna a size da array
print(array.shape, "\n")

array_dois = np.arange(0,10,1)
print(array_dois, "\n")

print(array_dois.shape, "\n")

array_tres = np.arange(0,10,0.25)
print(array_tres, "\n")

#vai ser util nem Machine learn e deep learn
print(np.zeros(10), "\n")
print(np.ones(10), "\n")
print(np.ones((2,2)), "\n")

#Cria uma matriz principal
array_quatro = np.eye(10)
print(array_quatro, "\n")

#Cria uma matriz principal recebedo um array de entrada
array_cinco = np.diag(np.array([1,2,3,4]))
print(array_cinco, "\n")

#criando uma matrix
array_cinco_partII = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(array_cinco_partII, "\n")

#Matriz 3 por 3
matriz_um = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz_um, "\n")
#descricao da matriz
print(matriz_um.shape, "\n")

#criando uma matriz por np.matriz recebendo uma lista, tb pode receber uma tupla
lista_aux = [[10,58,57],[25,34,69],[80,42,21]]
matriz_dois = np.matrix(lista_aux)
print(matriz_dois, "\n")

#retorna o tamanho gasto na memoria por cada item
print(matriz_dois.itemsize, "\n")

#retorna o tamanho gasto na memoria por todos os elementos
print(matriz_dois.nbytes, "\n")

#Imprimindo um elememento recebendo uma coordenada da matriz
print(matriz_dois[1,1], "\n")

#Imprimindo um elememento recebendo uma coordenada da matriz
matriz_dois[1,1] = 31
print(matriz_dois, "\n")

#np pega o tipo da entrada, mas np decida o tipo que vai ser
#mas é possivivel alterrar o tipo para um desejado, -> dtype = np.float64 ou -> dtype = np.int32
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
