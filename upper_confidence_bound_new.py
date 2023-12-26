# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 09:44:01 2023

@author: ivoto
"""
# Upper Confidence Bound (UCB)

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# Cargar el dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#Algoritmo Upper confidence bound 
N = 10000 #Es el numero de usuarios(rondas)
d = 10 #Numero de anuncios a mostrar (Clases) 
number_of_selections =   [0] * d #Lista que mantiene la cuenta de cuántas veces cada anuncio ha sido seleccionado hasta ahora.
sums_of_rewards = [0] * d #Lista que acumula las recompensas (clics) de cada anuncio.
ads_selected = [] #Lista para almacenar qué anuncio se selecciona en cada ronda.
total_reward = 0 #Variable para mantener el recuento total de las recompensas.
for n in range(0, N):
    max_upper_bound = 0
    ad = 0
    for i in range(0, d):
        if(number_of_selections[i]>0):
            average_reward = sums_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2*math.log(n+1)/number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
            
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
    
    
# Histograma de resultados
plt.hist(ads_selected)
plt.title("Histograma de anuncios")
plt.xlabel("ID del Anuncio")
plt.ylabel("Frecuencia de visualización del anuncio")
plt.show()
    