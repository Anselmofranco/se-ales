#señales con distinto tiempo de muestero y distinta pulsación

import numpy as np
import math as m
import matplotlib.pyplot as plt

paso_1=0.1 #frecuencia de muestreo = 10
t_1=np.arange (0,3,paso_1)
w_1=2*m.pi*5  #f=5hz

paso_2=0.1 #frecuencia de muestreo = 10
t_2=np.arange (0,3,paso_2)
w_2=2*m.pi*100  #f=100hz

paso_3=0.01 #frecuencia de muestreo = 100
t_3=np.arange (0,3,paso_3)
w_3=2*m.pi*5  #f=5hz

señal_1=np.sin(w_1*t_1) # es la señal analógica
señal_2=np.sin(w_2*t_2) # es la señal analógica
señal_3=np.sin(w_3*t_3) # es la señal analógica

plt.figure(1)
plt.plot(t_1,señal_1)

plt.figure(2)
plt.plot(t_2,señal_2)

plt.figure(3)
plt.plot(t_3,señal_3)


plt.show()



