import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def show_curve(kappa, s0, s1):
    Y0 = [0, 0, 0]
    xr = np.linspace(0, s1, 1000)
    xl = np.linspace(0, s0, 1000)
    def dY_ds(Y, s):
        return [kappa(s), np.cos(Y[0]), np.sin(Y[0])]
    Yr = odeint(dY_ds, Y0, xr)
    Yl = odeint(dY_ds, Y0, xl)
    yr1 = Yr[:,1]
    yr2 = Yr[:,2]
    yl1 = Yl[:,1]
    yl2 = Yl[:,2]
    plt.plot(yr1, yr2, yl1, yl2)
    plt.axis("equal")
    plt.show()

def kappa(s):
    return s**2

show_curve(kappa, -8, 8)