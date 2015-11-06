#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plot

N = 10000
X0 = np.random.rand(N)
# X1 = 3*X0
# Y  = np.power(9*X1, 1.0/3)
Y = np.power(27*X0, 1.0/3)

t = np.arange(0.0, 3.0, 0.01)
y = t*t/9

plot.plot(t, y, 'r-', linewidth=1)
plot.hist(Y, bins=50, normed=1, facecolor='green', alpha=0.75)
plot.show()
