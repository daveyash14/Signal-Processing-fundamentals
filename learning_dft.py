import numpy as np
import matplotlib.pyplot as plot

f1 = 10
f2 = 4000
f_s = 2*f1

t = np.linspace(0,2,2*f_s, endpoint=False)
#cos signal 
signal = np.cos(2*np.pi*f1*t) #+ np.cos(2*np.pi*f2*t)

#plotting the cosine wave
plot.plot(t, signal)
plot.show()