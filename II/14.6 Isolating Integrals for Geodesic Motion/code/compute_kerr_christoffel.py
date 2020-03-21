from gravipy.tensorial import Coordinates, MetricTensor, All, Christoffel
from sympy import *
from gravipy import *

t, phi, r, theta, m, a, sigma, delta, sigma_for_printing, delta_for_printing = symbols('t, \phi, r, \\theta, m, a, sigma, delta, Sigma, Delta')
# chi is 4 vector of coords
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

translate={1: "t", 2: "r", 3: "\\theta", 4: "\phi"}

for i in range(1,5):
    for j in range(1,5):
        for k in range(j,5):
            symbol = Gamma(-i,j,k)
            for l in range(1,5):
                symbol = symbol.subs(r ** 2 + (a ** 2) * cos(theta) ** 2, sigma_for_printing)
                symbol = symbol.subs(r ** 2 - 2 * m * r + a ** 2, delta_for_printing)
                symbol = symbol.expand()
                symbol = symbol.simplify()
                symbol = symbol.trigsimp()
            if symbol !=0:
                print("\Gamma^"+ translate[i]+"_{" + translate[j] + translate[k] + "} = " + latex(symbol) + r"\\")

