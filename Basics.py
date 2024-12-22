# Importing matplotlib, numpy and pandas library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) # Gives evenly spaced 100 values that lie in between 0 and 10
y = np.sin(x) # Finds sin value of x
z = np.cos(x) # Finds cos value of x

# Plotting the data

# Sine wave 
plt.plot(x, y)
plt.show()

# Cosine wave
plt.plot(x, z)
plt.show()

# Adding X-axis and Y-axis labels
plt.plot(x, y)
plt.xlabel('Angle')
plt.ylabel('Sine value')
plt.title('Sine Wave')
plt.show()

# Parabola
x = np.linspace(-10, 10, 20)
y = x**2 # x square
plt.plot(x, y)
plt.show()

# Plot with different symbols

plt.plot(x, y, 'r+') # Plot in red color with symbol +
plt.show()

plt.plot(x, y, 'g.') # Plot in green color with symbol .
plt.show()

# Plot multiple lines in a single graph
x = np.linspace(-5, 5, 50)
plt.plot(x, np.sin(x), 'r-')
plt.plot(x, np.cos(x), 'k--')
plt.title('Sine and Cosine waves')
plt.show()







