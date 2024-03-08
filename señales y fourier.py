#señal formada con distintos armónicos y muestreo según transformada de fourier

import numpy as np
import math as m
import matplotlib.pyplot as plt

t=np.arange(-2,2,0.01)


s=np.zeros(len(t))

for n in range(1,10):
    s=s+((-2/n)*np.cos(n*m.pi)+np.sin(n*t))

fs=np.fft.rfft(s)   #transformada de fourier    

plt.figure(1)
plt.plot(t,s)    

plt.figure(2)
plt.plot(abs(fs))

plt.show()
