from gravipy.tensorial import Coordinates, MetricTensor, All, Christoffel
from sympy import *
from gravipy import *
import math
from geodesic import *
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties

t, phi, r, theta, m = symbols('t, \phi, r, \\theta, m')
# chi is 4 vector of coords
x = Coordinates('\chi', [t, r, theta, phi])
Metric = diag(-(1-2*m/r), 1/(1-2*m/r), r**2, r**2*sin(theta)**2)
g = MetricTensor('g', x, Metric)
Gamma = Christoffel('Gamma', g)

translate={1: "t", 2: "r", 3: "\\theta", 4: "\phi"}

for i in range(1,5):
    for j in range(1,5):
        for k in range(j,5):
            symbol = Gamma(-i,j,k)
            for l in range(1,5):
                symbol = symbol.simplify()
            if symbol !=0:
                print("\Gamma^"+ translate[i]+"_{" + translate[j] + translate[k] + "} = " + latex(symbol) + r"\\")


#added 0 to not intefere with symbolic variables
E=0.97
m0=1
L=4
r0=15
theta0=math.pi/2
rprime0=0

#compute initial derivatives
thetaprime0 = math.sqrt((-1 + E**2/(1-2*m0/r0) - L**2/r0**2)/(r0**2))
tprime0 = -E/(1-2*m0/r0)
phiprime0 = L/(r0**2)

solution, tau = integrate(0, r0, theta0, 0, tprime0, rprime0, thetaprime0, phiprime0, 1,0, Gamma)

#int indicates integrated results
t_int= solution[:, 0]
tprime_int = solution[:, 1]
r_int = solution[:, 2]
rprime_int = solution[:, 3]
theta_int = solution[:, 4]
thetaprime_int = solution[:, 5]
phi_int = solution[:, 6]
phiprime_int = solution[:, 7]

E_int=[]
L_int=[]
for i in range(len(t_int)):
    E_int.append((g(1,1)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*tprime_int[i] + (g(1,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*phiprime_int[i])
    L_int.append(-((g(1,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*tprime_int[i] + (g(4,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*phiprime_int[i]))



figure(1, figsize=(6, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, t_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('t')
savefig('t', dpi=100)

figure(2, figsize=(6, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, r_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('r')
savefig('r', dpi=100)


figure(3, figsize=(4, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, theta_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('theta')
savefig('theta', dpi=100)


figure(4, figsize=(6, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, phi_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('phi')
savefig('phi', dpi=100)

figure(5, figsize=(6, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, E_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('E')
savefig('E', dpi=100)



figure(7, figsize=(6, 4.5))
xlabel('tau')
grid(True)
lw = 1
plot(tau, L_int, 'g', linewidth=lw)
legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
title('L')
savefig('L', dpi=100)




