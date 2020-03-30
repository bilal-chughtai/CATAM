from gravipy.tensorial import Coordinates, MetricTensor, All, Christoffel
from sympy import *
from gravipy import *


smalldelta, E, L, t, phi, r, theta, m, a, sigma, delta, sigma_for_printing, delta_for_printing, tdot, phidot, rdot, thetadot = symbols(r'\delta, E, L, t, \phi, r, \theta, m, a, sigma, delta, Sigma, Delta, \dot{t}, \dot{\phi}, \dot{r}, \dot{\theta}')
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
print("gamma computed")


y = [tdot, rdot, thetadot, phidot]
thetadotdot=0
for j in range(1, 5):
    for k in range(1, 5):

        #simplify first
        symbol = Gamma(-3,j,k)
        for l in range(1, 5):
            symbol = symbol.subs(r ** 2 + (a ** 2) * cos(theta) ** 2, sigma_for_printing)
            symbol = symbol.subs(r ** 2 - 2 * m * r + a ** 2, delta_for_printing)
            symbol = symbol.subs(
                sigma_for_printing * a ** 2 + sigma_for_printing * r ** 2 - 2 * a ** 2 * m * r * cos(
                    theta) ** 2 - 2 * m * r ** 3, sigma_for_printing * delta_for_printing)
            symbol = symbol.simplify()
        # to factorise product of delta and sigma
        symbol = symbol.subs(
            sigma_for_printing * a ** 2 + sigma_for_printing * r ** 2 + 2 * a ** 2 * m * r * sin(
                theta) ** 2,
            sigma_for_printing * delta_for_printing + 2 * a ** 2 * m * r + 2 * m * r ** 3)
        symbol = symbol.simplify()

        for l in range(1, 5):
            symbol = symbol.subs(r ** 2 + (a ** 2) * cos(theta) ** 2, sigma_for_printing)
            symbol = symbol.subs(r ** 2 - 2 * m * r + a ** 2, delta_for_printing)
            symbol = symbol.subs(
                sigma_for_printing * a ** 2 + sigma_for_printing * r ** 2 - 2 * a ** 2 * m * r * cos(
                    theta) ** 2 - 2 * m * r ** 3, sigma_for_printing * delta_for_printing)
            symbol = symbol.simplify()

        symbol = symbol.subs(
            sigma_for_printing * a ** 2 + sigma_for_printing * r ** 2 + 2 * a ** 2 * m * r * sin(
                theta) ** 2,
            sigma_for_printing * delta_for_printing + 2 * a ** 2 * m * r + 2 * m * r ** 3)
        symbol = symbol.simplify()




        thetadotdot += - symbol * y[j - 1] * y[k - 1]  # -1 as python list
        thetadotdot = thetadotdot.simplify()
        thetadotdot = thetadotdot.subs(r ** 2 + (a ** 2) * cos(theta) ** 2, sigma_for_printing)
        thetadotdot = thetadotdot.subs(r ** 2 - 2 * m * r + a ** 2, delta_for_printing)
        print(thetadotdot)


print(latex(thetadotdot))
Qdot = 2*(a*E*sin(theta)-L/sin(theta))*(a*E*cos(theta)+L*cos(theta)/(sin(theta)**2)) + 2*thetadotdot*sigma_for_printing**2 + 2*thetadot*(2*r*rdot-a**2*2*cos(theta)*sin(theta)*thetadot)*sigma_for_printing - smalldelta * a**2 * 2 * cos(theta) * sin(theta)
Qdot = Qdot.subs([(E,g(1,1)*tdot+g(1,4)*phidot),(L,-(g(1,4)*tdot+g(4,4)*phidot))])
Qdot = Qdot.subs(r ** 2 + (a ** 2) * cos(theta) ** 2, sigma_for_printing)
Qdot = Qdot.subs(r ** 2 - 2 * m * r + a ** 2, delta_for_printing)
Qdot=Qdot.simplify()
Qdot=Qdot.simplify()
Qdot=Qdot.simplify()



print(latex(Qdot))