import math

from scitools.StringFunction import StringFunction
from math import *


class Function:
    def __init__(self, input):
        self.function = StringFunction(input)
        self.input = input

    def evaluate(self, value):
        return self.function(value)

    def evaluate2(self, value):
        x = value
        return eval(self.input)


class Newton:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, xi, niter, fun, dfun, type_error=1):

        fun = Function(fun)
        dfun = Function(dfun)

        fx = fun.evaluate2(xi)
        dfx = dfun.evaluate2(xi)

        if fx == 0:
            return str(fx) + " is a root."
        if dfun == 0:
            return "The derivate can't be 0"

        contador = 0
        error = tol + 1

        self.values.append([contador, str(xi), str(
            "{:.2e}".format(fx)), str(dfx), None])

        while error > tol and fx != 0 and dfx != 0 and contador < niter:
            xn = xi - (fx/dfx)
            fx = fun.evaluate2(xn)
            dfx = dfun.evaluate2(xn)

            if type_error == 0:
                error = abs(xn-xi)
            else:
                error = abs((xn-xi)/xn)

            xi = xn

            contador = contador + 1
            self.values.append([contador, str(xn), str(
                "{:.2e}".format(fx)), str(dfx), str("{:.2e}".format(error))])

        if fx == 0:
            return f"{xi} is a root"
            
        elif error < tol:
            return f"{xn} its an aproximation to a root with a tolerance of {tol}"
        elif dfx == 0:
            return f"{xn} Possible multiple root"
        else:
            return f"Failed after {niter} iterations"

    def tabla_values(self):
        return self.values