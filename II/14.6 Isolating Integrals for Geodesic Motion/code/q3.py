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

#schwarzchild - for question 3 it is quite a bit faster to use this, even though could sub a=0
t, phi, r, theta, m, a = symbols('t, \phi, r, \\theta, m, a') #a included so we dont have to rewrite code for kerr
x = Coordinates('\chi', [t, r, theta, phi])
Metric = diag((1-2*m/r), -1/(1-2*m/r), -r**2, -r**2*sin(theta)**2)


#kerr - for question 4
# t, phi, r, theta, m, a, sigma, delta = symbols('t, \phi, r, \\theta, m, a, sigma, delta')
# x = Coordinates('\chi', [t, r, theta, phi])
# sigma = r ** 2 + (a ** 2) * cos(theta) ** 2
# delta = r ** 2 - 2 * m * r + a ** 2
#
# Metric = Matrix([[(1 - (2 * m * r) / sigma), 0, 0, (2 * a * m * r * sin(theta) ** 2) / sigma], [0, -
# sigma / delta, 0, 0], [0, 0, - sigma, 0], [(2 * a * m * r * sin(theta) ** 2) / sigma, 0, 0, -(sin
#                                                                                               (theta) ** 2) * (
#                                                        (r ** 2 + a ** 2) + (
#                                                            2 * (a ** 2) * m * r * sin(theta) ** 2) / sigma)]])


g = MetricTensor('g', x, Metric)
Gamma = Christoffel('Gamma', g)


def print_out_christoffel(Gamma):
    translate = {1: "t", 2: "r", 3: "\\theta", 4: "\phi"}
    for i in range(1,5):
        for j in range(1,5):
            for k in range(j,5):
                symbol = Gamma(-i,j,k)
                symbol = symbol.subs(a,0)
                for l in range(1,5):
                    symbol = symbol.simplify()
                if symbol !=0:
                    print("\Gamma^"+ translate[i]+"_{" + translate[j] + translate[k] + "} = " + latex(symbol) + r"\\")


def compute_one_geodesic(E,m0,a0,L,r0,theta0, rdot0, g, Gamma):
    #added 0 to not intefere with symbolic variables


    #compute initial derivatives
    gphiphi = (g(4, 4)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])
    gtphi = (g(1, 4)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])
    gtt = (g(1, 1)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])
    gthetatheta = (g(3, 3)).subs([(m, 1), (r, r0), (a, a0), (theta, theta0)])

    thetadot0=sqrt((1-(E**2*gphiphi+L**2*gtt+2*E*L*gtphi)/(gtt*gphiphi-gtphi**2))/gthetatheta)
    tdot0=(E*gphiphi+L*gtphi)/(gtt*gphiphi-gtphi**2)
    phidot0=-(E*gtphi+L*gtt)/(gtt*gphiphi-gtphi**2)



    #thetadot0 = math.sqrt((-1 + E**2/(1-2*m0/r0) - L**2/r0**2)/(r0**2))
    #tdot0 = -E/(1-2*m0/r0)
    #phidot0 = -L/(r0**2)

    solution, tau = integrate(0, r0, theta0, 0, tdot0, rdot0, thetadot0, phidot0, m0, a0, Gamma)

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
    Veffcons=[]



    for i in range(len(t_int)):
        gphiphi = (g(4, 4)).subs([(r, r_int[i]), (m, m0), (a, a0), (theta, theta_int[i])])
        grr = (g(2, 2)).subs([(r, r_int[i]), (m, m0), (a, a0), (theta, theta_int[i])])
        gtphi = (g(1, 4)).subs([(r, r_int[i]), (m, m0), (a, a0), (theta, theta_int[i])])
        gtt = (g(1, 1)).subs([(r, r_int[i]), (m, m0), (a, a0), (theta, theta_int[i])])
        gthetatheta = (g(3, 3)).subs([(r, r_int[i]), (m, m0), (a, a0), (theta, theta_int[i])])
        E_int.append(gtt*tdot_int[i] + gtphi*phidot_int[i])
        L_int.append(-(gtphi*tdot_int[i] + gphiphi*phidot_int[i]))
        Veffcons.append(grr*rdot_int[i]**2 +  gthetatheta*thetadot_int[i]**2 + (-1+(E_int[i]**2*gphiphi+L**2*gtt+2*E_int[i]*L_int[i]*gtphi)/(gtt*gphiphi-gtphi**2)))


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

    figure(8, figsize=(6, 4.5))
    xlabel(r'$\tau$')
    ylabel(r'$g_{rr}\dot{r}^2+g_{\theta\theta}\dot{\theta}^2 + V_{eff}(r, \theta, E, L_z)$')
    lw = 1
    plot(tau, Veffcons, 'g', linewidth=lw)
    savefig('Veff', dpi=100)

    return r_int, theta_int, rdot_int

#3
#print_out_christoffel(Gamma)

#3a:E,m0,a0,L,r0,theta0, rdot0, g, Gamma
#compute_one_geodesic(E=0.97, m0=1, a0=0, L=4, r0=15,theta0=math.pi/2,rdot0=0, g=g, Gamma=Gamma)

#3b/4
# r_cross = []
# rdot_cross = []
# r_int, theta_int, rdot_int = compute_one_geodesic(E=0.97, m0=1, L=4, r0=12,theta0=pi/2,rdot0=0, g=g, a0=0, Gamma=Gamma)
# for i in range(len(r_int)-1):
#     if theta_int[i + 1] > pi/2 > theta_int[i]:
#         r_cross.append((r_int[i+1]+r_int[i])/2)
#         rdot_cross.append((rdot_int[i+1] + rdot_int[i]) / 2)
#
#
# figure(9, figsize=(6, 4.5))
# plt.scatter(r_cross, rdot_cross, label='skitscat', color='k', s=25, marker="o")
# plt.tight_layout()
# plt.xlabel(r'$r$')
# plt.ylabel(r'$\dot{r}$')
# savefig('scatter', dpi=100)





