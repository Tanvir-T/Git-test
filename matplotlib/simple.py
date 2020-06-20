from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y, label='sin curve')
plt.plot(x,y2, label='cos curve')
plt.xlabel("angle")
plt.ylabel("curve")
plt.title('sin and cosine wave')
plt.legend()
plt.grid(color='r', linestyle='-')
plt.show()
