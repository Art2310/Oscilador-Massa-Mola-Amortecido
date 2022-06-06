# -*- coding: utf-8 -*-
"""ProgramaMassaMola.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFFjCqsmFQvnArM3G45UK-yeFwty8F6k
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

posinicial = float(input(" Digite a posição x inicial do bloco em metros: "))
p = float(input(" Considerando que quanto menor o intervalo maior será a precisão, digite o intervalo de \n"+
"tempo entre cada ponto do gráfico da posição que será gerado em segundos: "))
m = float(input(" Digite a massa m do bloco em kilogramas:"))
b = float(input(" Digite um valor para o coeficiente de atrito b em kg/s:"))
k = float(input(" Digite a constante elástica k em N/m:"))

# Obtendo a amplitude e a posição ângular inicial
if posinicial > 0:
  xm = posinicial
  posang = 0
  
else:
  xm = posinicial*(-1)
  posang = np.pi
# Obtendo a frenquência ângular do oscilador
w = np.sqrt(((4*k)-(b**2))/(4*m))
# Número de euler
e = 2.71828
# A lista a seguir irá armazenar a amplitude das cristas do gráfico
cristas = []
# Definindo x(t)
def x(t):
  r1 = xm*(e**(((-1)*b*t)/(2*m)))
  r2 = np.cos((w*t) + posang)
  result = r1 * r2
  if (r2 < 1.05) & (r2 > 0.95):
    cristas.append(result)
  return result
# Gerando gráfico
abscissas = []
ordenadas = []
raizes = []
i = 0
t = 0
ordenadas.append(posinicial)
abscissas.append(t)
while True:
  u = len(cristas)
  i += 1
  t += p
  abscissas.append(t)
  ordenadas.append(x(t))
# A seguir é testado se a ordenada obtida na iteração faz parte da lista cristas
  if len(cristas) > u:
# A seguir é testado se a crista suficientemente próxima de 0 para finalizar o loop
    if (ordenadas[i] < 0.01):
      break
plt.plot(abscissas,ordenadas)

