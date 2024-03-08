#señal creada a paartir de distintas frecuencias y uso de transformada de Fourier


import numpy as np
import math
import matplotlib.pyplot as plt

t=np.arange(-2,2,0.01)

s=np.cos(2*math.pi*20*t)+np.cos(2*math.pi*10*t)+2*np.cos(2*math.pi*5*t)
fs=np.fft.rfft(s)

plt.figure(1)
plt.plot(t,s)
plt.show()

plt.figure(2)
plt.plot(abs(fs))