import matplotlib.pyplot as plt
#import math
import numpy as np

# DETTE ER EN KOMMENTAR

plt.close('all') # close all figures

x = np.linspace(np.pi/2, np.pi, 1001)
x1 = [0.5, 0.5]
x2 = [0.6, 0.6]
y1 = [0 , 0.5]
y2 = [0 , 0.6]
plt.plot(np.sin(x), - np.cos(x))
plt.plot(np.sin(x1), -np.cos(y1))
plt.plot(np.sin(x2), -np.cos(y2))
plt.show()
