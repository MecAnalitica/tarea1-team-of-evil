#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Tarea I 
import numpy as np

def funcion(t):
    return ((k * V + g) / (g * k)) * (1 - np.exp(-k * t))

def derivada(t):
    return -((k * V + g) / g) * (np.exp(-k * t))

def derivada2(t):  
    return ((k**2 * V + g*k) / g) * (np.exp(-k*t)) 
    
    # Definición de variables
print ("Hola, este programa te da el tiempo de vuelo de una partícula con resistencia al aire (inciso a)")
k = float(input("Ingrese un valor para la constante de amortiguamiento: "))
v = float(input("Ingrese un valor para la velocidad inicial: "))
a = float(input("Ingrese un valor para el ángulo: "))   
g = 9.81

a = (a * np.pi) / 180 # Conversión de grados a radianes
V = v * np.sin(a) # Variable V


    # Método de Newton-Rapson para calcular el tiempo usando aproximaciones
t0 = 1  # Se sugiere una primera aproximación
error = 1 #  valor inicial de error

while error > 1e-6: # Condición para la exactitud
    t1 = t0 - funcion(t0)/derivada(t0)  
    error = abs((derivada2(t0)/2*derivada(t0))*(error**2))
    print("error: ", error) # Para corroborar que el error se cumpla
    t0 = t1 

print("tiempo: ", t1)
   

