import pygame
import math
import numpy as np
import matplotlib.pyplot as plt

points = []

for i in range(8):
    for j in range(8):
        for k in range(8):
            points.append([i, j, k, 0])

#plt.ion()
fig = plt.figure()
ax = plt.axes(projection='3d')

xdata = []
ydata = []
zdata = []
for p in points:
    xdata.append(p[0])
    ydata.append(p[1])
    zdata.append(p[2])

color = ["white" for i in points]

ax.scatter3D(xdata, ydata, zdata, color = color)

plt.show()

#color = ["red" for i in points]
#plt.draw()



