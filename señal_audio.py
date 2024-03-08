# Armar una señal con armónicos, mostrarla, transformarla con fourier y crear archivo .wav con dicha señal 
# Levantar un archivo .wav de un audio de una cuerda de guitarra y hacerle la transformada de Fourier

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

paso=1/44100.0 # frec muestreo = 44100 hz

t=np.arange(0,3,paso)
A=3000
w=440
s=A*np.cos(2*math.pi*w*t)+(A/2)*np.cos(2*math.pi*2*w*t)+(A/3)*np.cos(2*math.pi*3*w*t)
fs=np.fft.rfft(s)
samplerate, cuerda=wav.read("APrueba.wav")

plt.figure(1)
plt.plot(t[0:1000],s[0:1000])
plt.show()

plt.figure(2)
frecuencias=np.fft.rfftfreq(t.size,d=paso)
plt.plot(frecuencias[0:4000],abs(fs[0:4000]))
wav.write("tono2.wav",44100,s.astype(np.int16))  #s.as... devuelve el s como un número entero

plt.figure(3)
plt.plot(cuerda)

plt.figure(4)
fftcuerda=np.fft.rfft(cuerda)
freccuerda=np.fft.rfftfreq(cuerda.size,d=paso)
plt.plot(freccuerda[0:5000],abs(fftcuerda[0:5000]))
