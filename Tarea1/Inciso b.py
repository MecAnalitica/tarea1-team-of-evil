#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Inciso b
import numpy as np
import matplotlib.pyplot as plt


def funcion0(g, v, a):
    return ((v**2) / g) * (np.sin(2 * a))

def funcion(t, k, g, V):
    return ((k * V + g) / (g * k)) * (1 - np.exp(-k * t))

def derivada(t, k, g, V):
    return -((k * V + g) / g) * (np.exp(-k * t))

def derivada2(t, k, g, V):
    return ((k**2 * V + g*k) / g) * (np.exp(-k*t)) 

# Declaración de condiciones iniciales
g = 9.81
v = 500
a = (65 * np.pi) / 180
V = v * np.sin(a)

    # Para k=0
funcion0(g, v, a)
T0 = funcion0(g, v, a)
print("Tiempo con k=0: ", funcion0(g, v, a)) # Si sirve

    # Para k= 0.03
t0 = 1
error = 1
k = 0.03

while error > 1e-6:
    T1 = t0 - funcion(t0, k, g, V)/derivada(t0, k, g, V)
    error = abs((derivada2(t0, k, g, V)/2*derivada(t0, k, g, V))*(error**2))
    t0 = T1
        
print("Tiempo con k=0.03: ", T1)

    # Para k= 0.05
t0 = 1
error = 1
k = 0.05

while error > 1e-6:
    T2 = t0 - funcion(t0, k, g, V)/derivada(t0, k, g, V)
    error = abs((derivada2(t0, k, g, V)/2*derivada(t0, k, g, V))*(error**2))
    t0 = T2
        
print("Tiempo con k=0.05: ", T2)

    # Para k=0.075
t0 = 1
error = 1
k = 0.075

while error > 1e-6:
    T3 = t0 - funcion(t0, k, g, V)/derivada(t0, k, g, V)
    error = abs((derivada2(t0, k, g, V)/2*derivada(t0, k, g, V))*(error**2))
    t0 = T3
        
print("Tiempo con k=0.075: ", T3)

    # Para k= 0.09
t0 = 1
error = 1
k = 0.09

while error > 1e-6:
    T4 = t0 - funcion(t0, k, g, V)/derivada(t0, k, g, V)
    error = abs((derivada2(t0, k, g, V)/2*derivada(t0, k, g, V))*(error**2))
    t0 = T4
        
print("Tiempo con k=0.09: ", T4)

    # Para graficar
x = [0, 0.03, 0.05, 0.075, 0.09] #Valores de k
y = [T0, T1, T2, T3, T4] # Valores del tiempo
plt.plot(x, y)
plt.title("Rango vs k")
plt.xlabel("Constante k")
plt.ylabel("Rango")
plt.show()

    # Inciso C: Gráfica de la posición en x,y con diferentes k
x0 = v*np.cos(a)*T0
y0 = v*np.sin(a)*T0 -g*T0**2 /2

print("x para k=0: ", x0)
print("y para k=0: ", y0)

x1 = -(v * np.cos(a) / (0.03))*(np.exp(-(0.03 * T1)) - 1)
y1 = -(g / 0.03)*T1 - (((V * 0.03) + g) / (0.03)**2) * (np.exp(-0.03 * T1) - 1)

print("x para k=0.03: ", x1)
print("y para k=0.03: ", y1)

x2 = -(v * np.cos(a) / (0.05))*(np.exp(-(0.05 * T2)) - 1)
y2 = -(g / 0.05)*T2 - (((V * 0.05) + g) / (0.05)**2) * (np.exp(-0.05 * T2) - 1)

print("x para k=0.05: ", x2)
print("y para k=0.05: ", y2)

x3 = -(v * np.cos(a) / (0.075))*(np.exp(-(0.075 * T3)) - 1)
y3 = -(g / 0.075)*T3 - (((V * 0.075) + g) / (0.075)**2) * (np.exp(-0.075 * T3) - 1)

print("x para k=0.075: ", x3)
print("y para k=0.075: ", y3)

x4 = -(v * np.cos(a) / (0.03))*(np.exp(-(0.03 * T4)) - 1)
y4 = -(g / 0.09)*T4 - (((V * 0.09) + g) / (0.09)**2) * (np.exp(-0.09 * T4) - 1)

print("x para k=0.09: ", x4)
print("y para k=0.09: ", y4)

dx = [x0, x1, x2, x3, x4]
dy = [y0, y1, y2, y3, y4]

plt.plot(dx, dy)
plt.title("Posición en x VS Posición en y para distintos valores de k")
plt.xlabel("Posición en x")
plt.ylabel("Posición en y")
plt.show()

