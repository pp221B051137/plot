import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,-S)
plt.plot(X,-C)
plt.plot(X,S)
 
plt.plot(X,C)
val = [0,10,20,30,40,50,60]
plt.xticks (ticks=[-3,-2,-1,0,1,2,3], labels=val)

ax.set_facecolor('#eaeaf2')
plt.grid()
plt.show()