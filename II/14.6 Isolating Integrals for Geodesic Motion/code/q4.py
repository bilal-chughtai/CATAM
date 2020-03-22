import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


E=0.95
L=3
a=0.9

func = lambda r : 1 - (-E**2*(r**2+a**2+2*a**2/r)+L**2*(1-2/r)+4*E*L*a/r)/(4*a**2/r**2+(1-2/r)*(r**2+a**2+2*a**2/r))

r=np.linspace(-10, 10, 201)

plt.plot(r, func(r))
axes = plt.gca()
axes.set_ylim([-10,10])
plt.xlabel("r")
plt.ylabel("Veff")
plt.grid()
plt.show()

r_initial_guess = 1
r_solution = fsolve(func, r_initial_guess)
print(r_solution)