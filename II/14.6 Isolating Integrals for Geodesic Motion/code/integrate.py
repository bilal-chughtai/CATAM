from collections import defaultdict
from scipy.integrate import odeint
from sympy import *
from numpy import loadtxt
from matplotlib.font_manager import FontProperties

def integrate(t,r,theta,phi,tdot,rdot,thetadot,phidot, m0, a0, Gamma):
    # initial values inputted, as well as christoffel symbols


    def vectorfield(w, tau, p):
        t, phi, r, theta, m, a= symbols('t, \phi, r, \\theta, m, a')
        """
        Defines the differential equations, and outputs an f

        Arguments:
            w :  vector of the state variables:
                      w = [x1,y1,x2,y2,x3,y3,x4,y4]
            tau :  time
            p :  vector of the parameters:
                      p = [m]
        """
        x1, y1, x2, y2, x3, y3, x4, y4 = w
        x=[x1,x2,x3,x4]
        y=[y1,y2,y3,y4]
        m0 = p[0]
        a0 = p[1]

        #compute DE for yi:
        ydot=defaultdict(float)
        for i in range(1,5):
            for j in range (1,5):
                for k in range (1,5):
                    ydot[i] += (-Gamma(-i,j,k)).subs([(t,x1),(r,x2),(theta,x3), (phi,x4), (m,m0), (a,a0)])*y[j-1]*y[k-1] #-1 as python list

        # Create f = (x1',y1',x2',y2'):
        f = [y1,ydot[1],y2,ydot[2],y3,ydot[3],y4,ydot[4]]
        return f


    # Initial conditions
    # x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
    x1 = t
    y1 = tdot
    x2 = r
    y2 = rdot
    x3 = theta
    y3 = thetadot
    x4 = phi
    y4 = phidot

    # ODE solver parameters
    abserr = 1.0e-8
    relerr = 1.0e-6
    stoptime = 1200 #1200
    numpoints = 250

    # Create the time samples for the output of the ODE solver.
    # I use a large number of points, only because I want to make
    # a plot of the solution that looks nice.
    tau = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

    # Pack up the parameters and initial conditions:
    p = [m0,a0]
    w0 = [x1, y1, x2, y2, x3, y3, x4, y4]

    # Call the ODE solver.
    wsol = odeint(vectorfield, w0, tau, args=(p,),
                  atol=abserr, rtol=relerr)



    return wsol, tau