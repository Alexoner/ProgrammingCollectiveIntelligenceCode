#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plot

N = 50000
T1 = np.random.rand(N)
T2 = np.random.rand(N)

r = np.sqrt(-2*np.log(T2))
theta = 2*np.pi*T1
X = r*np.cos(theta)
Y = r*np.sin(theta)

heatmap, xedges, yedges = np.histogram2d(X, Y, bins=80)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plot.imshow(heatmap, extent=extent)
plot.show()
