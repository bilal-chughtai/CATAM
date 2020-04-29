from gravipy.tensorial import Coordinates, MetricTensor, All, Christoffel
from sympy import *
from gravipy import *
import math
from integrate import *
from pylab import figure, plot, xlabel, ylabel, grid, legend, title, savefig
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


#kerr - for question 4
t, phi, r, theta, m, a, sigma, delta = symbols('t, \phi, r, \\theta, m, a, sigma, delta')
x = Coordinates('\chi', [t, r, theta, phi])
sigma = r ** 2 + (a ** 2) * cos(theta) ** 2
delta = r ** 2 - 2 * m * r + a ** 2

Metric = Matrix([[(1 - (2 * m * r) / sigma), 0, 0, (2 * a * m * r * sin(theta) ** 2) / sigma], [0, -
sigma / delta, 0, 0], [0, 0, - sigma, 0], [(2 * a * m * r * sin(theta) ** 2) / sigma, 0, 0, -(sin
                                                                                              (theta) ** 2) * (
                                                       (r ** 2 + a ** 2) + (
                                                           2 * (a ** 2) * m * r * sin(theta) ** 2) / sigma)]])

g = MetricTensor('g', x, Metric)
Gamma = Christoffel('Gamma', g)



def compute_one_geodesic(E,m0,a0,L,r0,theta0,rdot0, g, Gamma):
    #added 0 to not intefere with symbolic variables


    #compute initial derivatives
    gphiphi=(g(4,4)).subs([(m,1),(r,r0),(a,a0),(theta,theta0)])
    gtphi = (g(1, 4)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])
    gtt = (g(1, 1)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])


    thetadot0 = math.sqrt((-1 + E**2/(1-2*m0/r0) - L**2/r0**2)/(r0**2))
    tdot0 = E*gphiphi
    phidot0 = -L/(r0**2)

    solution, tau = integrate(0, r0, theta0, 0, tdot0, rdot0, thetadot0, phidot0, 1, a0, Gamma)

    #int indicates integrated results
    t_int= solution[:, 0]
    tdot_int = solution[:, 1]
    r_int = solution[:, 2]
    rdot_int = solution[:, 3]
    theta_int = solution[:, 4]
    thetadot_int = solution[:, 5]
    phi_int = solution[:, 6]
    phidot_int = solution[:, 7]

    E_int=[]
    L_int=[]
    for i in range(len(t_int)):
        E_int.append((g(1,1)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*tdot_int[i] + (g(1,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*phidot_int[i])
        L_int.append(-((g(1,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*tdot_int[i] + (g(4,4)).subs([(r,r_int[i]), (m,m0), (theta,theta_int[i])])*phidot_int[i]))



    figure(1, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel('t')
    lw = 1
    plot(tau, t_int, 'g', linewidth=lw)
    savefig('t', dpi=100)

    figure(2, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel('r')
    lw = 1
    plot(tau, r_int, 'g', linewidth=lw)
    savefig('r', dpi=100)

    figure(3, figsize=(4, 4.5))
    xlabel(r'$\tau$')
    ylabel(r'$\theta$')
    lw = 1
    plot(tau, theta_int, 'g', linewidth=lw)
    savefig('theta', dpi=100)

    figure(4, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel(r'$\phi$')
    lw = 1
    plot(tau, phi_int, 'g', linewidth=lw)
    savefig('phi', dpi=100)

    figure(5, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel('E')
    lw = 1
    plot(tau, E_int, 'g', linewidth=lw)
    savefig('E', dpi=100)

    figure(7, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel(r'$L_z$')
    lw = 1
    plot(tau, L_int, 'g', linewidth=lw)
    savefig('L', dpi=100)

    return r_int, theta_int, rdot_int

#3
#print_out_christoffel(Gamma)

#3a:
#compute_one_geodesic(E=0.97, m0=1, L=4, r0=2.5,theta0=math.pi/2,rdot0=0, g=g, Gamma=Gamma)

#3b
r_cross = []
rdot_cross = []
r_int, theta_int, rdot_int = compute_one_geodesic(E=0.97, m0=1, L=4, r0=20,theta0=pi/2,rdot0=0, g=g, a0=0, Gamma=Gamma)
for i in range(len(r_int)-1):
    if theta_int[i + 1] > pi/2 > theta_int[i]:
        r_cross.append((r_int[i+1]+r_int[i])/2)
        rdot_cross.append((rdot_int[i+1] + rdot_int[i]) / 2)


figure(8, figsize=(6, 4.5))
plt.scatter(r_cross, rdot_cross, label='skitscat', color='k', s=25, marker="o")
plt.tight_layout()
plt.xlabel(r'$r$')
plt.ylabel(r'$\dot{r}$')
savefig('scatter', dpi=100)





