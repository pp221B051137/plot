import matplotlib.pyplot as plt
import numpy as np
x = np.random.uniform(0.02,0.6,21)
y = np.random.uniform(0.02,0.6,21)
print(x,y)
plt.plot([0.02,0.6],[0.02,0.6],c='red')
plt.scatter(x,y,c='blue')
plt.show()