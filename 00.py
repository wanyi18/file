import numpy as np
import random
import matplotlib.pyplot as plt
ns = 100 # no of steps
x = range(ns)
y = np.zeros(ns)
for i in x[1:]:
    coin = random.random()
    if coin < 0.525:
        y[i]=y[i-1]-1
    else:
        y[i]=y[i-1]+1
plt.plot(x, y)
plt.show() 
