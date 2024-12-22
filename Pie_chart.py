# Pie Chart

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure() # Creates an empty plot
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7]) # [left, bottom, width, height], encloses our plot in a rectangle
languages = ['English', 'Nepali', 'Hindi', 'Japanese', 'Latin']
people = [100, 20, 30, 25, 40]

ax.pie(people, labels = languages, autopct= '%1.1f%%')
plt.show()