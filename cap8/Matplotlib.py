import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import cm
from matplotlib import pylab
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.arange(20)
y = np.random.randint(0, 100, len(x))

plt.plot(x,y)
plt.title("Valores random")
plt.legend("Variação")
plt.xlabel("Array")
plt.ylabel("Valores por elemento")
plt.show()

plt.bar(x, y, label = "Variação", color = "b")
plt.title("Valores random")
plt.legend()
plt.xlabel("Array")
plt.ylabel("Valores por elemento")
plt.show()

indice = [x for x in range(len(x))]

plt.bar(indice, y)
plt.show()

# Barras paralelas

x2 = np.arange(0,20,2)
x3 = np.arange(1,20,2)
y2 = np.random.randint(0, 100, len(x2))
y3 = np.random.randint(0, 100, len(x3))

plt.bar(x2, y2, label = "Variação 1", color = "b")
plt.bar(x3, y3, label = "Variação 2", color = "y")
plt.legend()
plt.show()

# HISTOGRAMA

escala = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
array = [31,41,58,76,95,84,12,19,35,65,74,85,8,20,125,130,101,81,117]

# alpha -> define o tom da cor
plt.hist(array, escala, histtype = 'stepfilled', rwidth = 0.8, alpha=0.75)
plt.show()

# SCATTERPLOT

plt.scatter(x, y, label = "SCATTERPLOT", color = "g", marker = 'o', s = 100)
plt.legend()
plt.show()

# STACK PLOTS

dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,30]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ["r","g","y","b","c"])
plt.show()

# PIE CHART

partes = [15,40,30,11,9]
pern = ["Lanterna Verde", "Superman","Mulher Maravilha","Flash", "Cyborg"]
list_colors = ["g","r","y","b","c"]

plt.pie(partes, labels = pern, colors = list_colors, startangle = 90, shadow = True, explode = (0,0,0,0,0))
plt.show()

# PYLAB ->>>

x4 = np.linspace(0,5,10)
y4 = x4 ** 2

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,1,1])
axes.plot(x4, y4, "r")

# ---
y4_aux = x4 ** 3.5
fig2 = plt.figure()

axes2 = fig2.add_axes([0.1,0.1,1,1])
axes2.plot(x4, y4, "b")
axes2.set_xlabel("X principal")
axes2.set_ylabel("Y principal")

axes3 = fig2.add_axes([0.25,0.7,0.4,0.3])
axes3.plot(x4, y4_aux, "y")
axes3.set_xlabel("X Segundario")
axes3.set_ylabel("Y Segundario")


# ---
fig3, axes = plt.subplots(nrows = 1, ncols = 2)
for ax in axes:
    ax.plot(x, y, "r")

fig3.tight_layout() 

# Graficos atraves do Numpy

plt.scatter(np.arange(50), np.random.randn(50))
plt.show()

# ---
fig4 = plt.figure()

graf1 = fig4.add_subplot(1,2,1)
graf1.plot(np.random.randn(50), color = 'red')

graf2 = fig4.add_subplot(1,2,2)
graf2.scatter(np.arange(50), np.random.randn(50))
plt.show()


# ---
# Pode também colocar tudo em uma matriz, cada elemento um possivel grafico 
_, ax = plt.subplots(2, 4, figsize = (12, 6))

ax[0,1].plot(np.random.randn(50), color = 'red', linestyle = '-')
ax[0,3].bar(np.arange(50), np.random.randn(50), color = "y")
ax[1,0].hist(np.random.randn(50), color = "blue")
ax[1,2].scatter(np.arange(50), np.random.randn(50), color = 'green')
plt.show()

# Controle dos eixos

fig5, axes = plt.subplots(1, 3, figsize = (14, 5))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("Eixos com range padrão")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("Eixos menores")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("Eixos customizados");
plt.show()

# Escalas --> ainda vou resolver 
'''fig, axes = plt.subplots(1, 2, figsize=(10,4))
      
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title("Escala Padrão")

axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Escala Logaritmica (y)");'''


# Grid
fig6, axes = plt.subplots(1, 2, figsize = (14, 5))

# Grid padrão
# lw = 2 -> Espessura da linha igual a 2
axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

# Grid customizado
# linewidth = 0.5 -> tamanho dos traço,  alpha = 0.5 -> opacocidade

axes[1].plot(x, x**2.5, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.5)
plt.show()

# Varios Plots um um array

x_b = np.linspace(0, 1, 100)
aux_x = np.array([0,1,2,3,4,5])

fig7, axes = plt.subplots(1, 5, figsize = (14, 5))

axes[0].scatter(x_b, x_b + (0.25 * np.random.randn( len(x_b) )))
axes[0].set_title("Scatter")

axes[1].step(aux_x, (aux_x ** 2), lw = 2)
axes[1].set_title("Step")

axes[2].bar(aux_x, (aux_x ** 2), align = "center", width = 0.5, alpha = 0.5)
axes[2].set_title("Bar")

axes[3].fill_between(x_b, (x_b ** 2), (x_b ** 3), color = "green", alpha = 0.5);
axes[3].set_title("Between");

axes[4].plot(aux_x, (aux_x ** 2), lw = 2)
axes[4].set_title("Plot")
plt.show()

# Histogramas

random = np.random.randn(500)
fig8, sem_nome_legal = plt.subplots(1, 2, figsize = (14, 5))

sem_nome_legal[0].hist(random)
sem_nome_legal[0].set_title("Histograma Padrão")
sem_nome_legal[0].set_xlim((min(random), max(random)))

sem_nome_legal[1].hist(random, cumulative = True, bins = 50)
sem_nome_legal[1].set_title("Histograma Cumulativo")
sem_nome_legal[1].set_xlim((min(random), max(random)));
plt.show()

# GRAFICOS 3D ->>

X = list(np.linspace(0, 4, 100))
Y = list(np.linspace(0, 4, 100))
X, Y = np.meshgrid(X, Y)
Z =  np.array( X * Y )

fig9 = plt.figure(figsize = (14, 5))

# rstride, cstride and linewidth -> Definem a transparencia do resultado e das linhas do grafico
tresD_um = fig9.add_subplot(1, 2, 1, projection = '3d')
GrafP = tresD_um.plot_surface(X, Y, Z, rstride = 4, cstride = 4, linewidth = 0)

# cm.coolwarm -> muda a aparencia
tresD_um = fig9.add_subplot(1, 2, 2, projection = '3d')
GrafP = tresD_um.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0, antialiased = True)

# colorbar() -> Gera um indice lateral
cb = fig9.colorbar(GrafP, shrink = 0.5)
plt.show()

# ---
fig10 = plt.figure(figsize = (10, 6))

tresD_dois = fig10.add_subplot(1, 1, 1, projection = '3d')
Grafg = tresD_dois.plot_wireframe(X, Y, Z, rstride = 4, cstride = 4, linewidth = 2, alpha=0.25)
tabela_dois = fig10.colorbar(Grafg, shrink = 0.5)
plt.show()


