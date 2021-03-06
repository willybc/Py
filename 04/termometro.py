# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:22:04 2020

@author: WILLY
"""

import random
import numpy as np

temperatura = 37.5
MU = 0
SIGMA = 0.2

N= 999

temperaturas = [ random.normalvariate( MU, SIGMA) + temperatura for i in range(N) ]

np.savetxt('../Data/Temperaturas.npy', temperaturas)

maxi = max(temperaturas)
mini = min(temperaturas)
prom = sum(temperaturas)/len(temperaturas)

print(f' Maximo = {maxi}')
print(f' Minimo = {mini}')
print(f' Promedio = {prom}')

temperaturas.sort()
posicion_central = int(((N-1)/2)+1)
print(temperaturas[posicion_central])

