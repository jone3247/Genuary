# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:46:00 2022

@author: marie
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

savepath = 'D:/1_DesktopBackup/Art/Art Code/art-projects/hitomezashi-stitches/figs/'

#Prompt: Black and White (also meshing with Jan 18 prompt: Definitely not a grid)

''' Randomly generate plots of Hitomezashi patterns '''

# Fixing random state for reproducibility
np.random.seed(48493)

N = 30
p = 0.5 #probability of success

#Generate grid to plot on
X = np.linspace(1, N, N, endpoint = True)
Y = np.linspace(1, N, N, endpoint = True)
xx, yy = np.meshgrid(X, Y)

'''Plotting'''
# Create new Figure with black background
fig = plt.figure(figsize=(10, 10), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
plt.plot(xx, yy, marker = '.', color = 'white', linestyle = 'none') #Grid points
#plt.show()

'''Animating'''
#t = 10e-7
k = 1
#Plot Horizontal lines
for i in range(1, N+1):
    #Generate bit
    r = np.random.rand(1, 1)
    #Travel along the X axis one Y at a time and draw lines connecting dots
    if r < p:
        #Start on
        for j in range(1, N):
            if j%2 == 1:
                plt.plot([j, j+1], [i, i], color = 'white', linestyle = '-')
                #plt.pause(t)
                plt.savefig(savepath + f'line-{k}.png')
                k = k+1
    else:
        #Start off
        for j in range(1, N):
            if j%2 == 0:
                plt.plot([j, j+1], [i, i], color = 'white', linestyle = '-')
                #plt.pause(t)
                plt.savefig(savepath + f'line-{k}.png')
                k = k+1

#Plot Vertical lines
for i in range(1, N+1):
    #Generate bit
    r = np.random.rand(1, 1)
    #Travel along the X axis one Y at a time and draw lines connecting dots
    if r < p:
        #Start on
        for j in range(1, N):
            if j%2 == 1:
                plt.plot([i, i], [j, j+1], color = 'white', linestyle = '-')
                #plt.pause(t)
                plt.savefig(savepath + f'line-{k}.png')
                k = k+1
    else:
        #Start off
        for j in range(1, N):
            if j%2 == 0:
                plt.plot([i, i], [j, j+1], color = 'white', linestyle = '-')
                #plt.pause(t)
                plt.savefig(savepath + f'line-{k}.png')
                k = k+1

plt.show()
        
#%%

''' Maybe make animation of small changes to the generated two bit strings'''
import imageio

with imageio.get_writer(savepath + 'line.gif', mode = 'i', fps = 20) as writer:
    for i in range(1, k+1):
        image = imageio.imread(savepath + f'line-{i}.png')
        writer.append_data(image)
# %%
