# Scatter plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
ax.scatter(x, y, color='r')
ax.scatter(x, z, color='k')
plt.show()

# 3D Scatter plot

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
z = 20 * np.random.rand(50)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x, y, z, c=z, cmap='Reds')
plt.show()

