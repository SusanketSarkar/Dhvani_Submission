import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def function(ini, t):
    a, b, c = 10, 28, 2.667
    x, y, z = ini[0], ini[1], ini[2]
    dxdt = a*(y-b)
    dydt = b*x-y-x*z
    dzdt = x*y - c*z
    return [dxdt, dydt, dzdt]

t = np.linspace(0,2.5)
ini=[0,1,1.05]
s = odeint(function,ini,t)

plt.plot(t,s[:,0],'r-', linewidth=2.0)
plt.plot(t,s[:,1],'b-', linewidth=2.0)
plt.plot(t,s[:,2],'k-', linewidth=2.0)

plt.legend(["x","y", "z"])
plt.show()