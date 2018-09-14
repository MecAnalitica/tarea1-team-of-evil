
# coding: utf-8

# ### !/usr/bin/env python
# # coding: utf-8
# 
# # In[11]:
# 
# 
# # Tarea I 
# import numpy as np
# from numpy import array
# from numpy import * 
# def fx(t):
#     return ((-vc0) / (k)) * (np.exp(-k * t) - 1)
# 
# def dfx(t):
#     return -((vs0) / k) * (np.exp(-k * t) - 1)
# 
#     
#     # Definición de variables
# print ("Hola, este programa te da el tiempo de vuelo de una partícula con resistencia al aire (inciso a)")
# k = float(input("Ingrese un valor entre 0 y 1 para la constante de amortiguamiento: "))
# v = float(input("Ingrese un valor para la velocidad inicial: "))
# #a = float(input("Ingrese un valor para el angulo: "))   
# g = 9.81
# 
# a = (a * np.pi) / 180 # Conversión de grados a radianes
# vc0 = v*np.cos(a) # Variable V
# vs0 = v* np.sin(a)
# 
#     # Método de Newton-Rapson para calcular el tiempo usando aproximaciones
# t0 = 1  # Se sugiere una primera aproximación
# 
# i = int(0)
# v = []
# #v[0] = 0
# #v = np.atrray([i])
# 
# error = 1 # condición de error
# 
# while error > 1**-6:
#     t1 = t0 - fx(t0) / dfx(t0)
#     error = abs(t1 - t0)
#     t0 = t1
#     v.append(t1)
#     i = i+1
#  
# 
# print("El tiempo de vuelo de la particula ha sido de: ", t1)
# th = np.asin((k)(v*(np.exp(-k * t) - 1)))
# 
# print("Dado ese tiempo, su ángulo de alcance máximo theta es de:" , th )
# 
# 
