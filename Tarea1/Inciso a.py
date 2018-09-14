#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Tarea I 

import numpy as np

def funcion(t):
    return ((k*vy+g)/(g*k))*(1-np.exp(-k*t))

def derivada(t):
    return -((k*vy+g)/g)*(np.exp(-k*t))
    
    # Definición de variables
print ("Hola, este programa te da el tiempo de vuelo de una partícula con resistencia al aire (inciso a)")
k = float(input("Ingrese un valor para la constante de amortiguamiento "))
v = float(input("Ingrese un valor para la velocidad inicial "))
a = float(input("Ingrese un valor para el ángulo "))   
g = 9.81

vy = v*np.sin(a)

    # Método de Newton-Rapson
t0= 1 # De donde empieza
error = 1 # condición de error

while error > 1**-6:
    t1 = t0 - funcion(t0) / derivada(t0)
    error = abs(t1 - t0)
    t0 = t1
    print(t0)

print("Tiempo de vuelo= ", t0)

