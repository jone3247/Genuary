# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:46:00 2022

@author: marie
"""

#Prompt: Create your own pseudo-random number generator and visually check the results.

''' 2D Random Walk on a beige background '''

import random as rand
import numpy as np
import matplotlib.pyplot as plt

for j in range(0, 5):
    n = 1000 #steps to take
    
    x = np.zeros(n)
    y = np.zeros(n)
    
    for i in range(1, n):
        m = rand.randint(0, 3)
        
        #0 --> y is constant, x increases
        #1 --> y increases, x is constant
        #2 --> y is constant, x decreases
        #3 --> y decreases, x is constant
        
        if(m == 0):
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
        if(m == 1):
            x[i] = x[i-1] 
            y[i] = y[i-1] + 1
        if(m == 2):
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        if(m == 3):
            x[i] = x[i-1] 
            y[i] = y[i-1] - 1
            
    #plot
    plt.style.use('dark_background')
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.triplot(x, y, color = 'white')
    
    plt.savefig(r"C:\Users\marie\Desktop\Art Code\Jan24_" + str(j) +".pdf")


