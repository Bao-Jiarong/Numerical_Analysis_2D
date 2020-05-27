'''
 *  Author : Bao Jiarong
 *  Contact: bao.salirong@gmail.com
 *
 *  Created  On: 2020-05-27
 *  Modified On: 2020-05-27
 '''
from .algo import *

class NA(Algo):
    #----------------------------------------------------------
    # Constructor
    #----------------------------------------------------------
    def __init__(self,a,b,T,f,df=None,ddf=None,eps=1e-3,verbose=False):
        Algo.__init__(self,T,f,eps,verbose)
        self.x0  = a
        self.x1  = b
        self.df  = df
        self.ddf = ddf

    #----------------------------------------------------------
    # Bisection Method
    # Info (En): https://en.wikipedia.org/wiki/Bisection_method
    # Info (Ch): https://zh.wikipedia.org/wiki/二分法_(數學)
    #----------------------------------------------------------
    def bisection(self):
        self.err = []
        x = (self.x0 + self.x1)/2

        for t in range(self.T):
            # Algorithm
            prev = x
            x    = (self.x0 + self.x1) / 2

            if abs(self.f(x)) < self.eps or (self.x1 - self.x0) / 2 < self.eps:
                break

            if self.f(x) * self.f(self.x0) >= 0:
                self.x0 = x
            else:
                self.x1 = x

            # Loss
            error = abs(prev - x)
            self.err.append(error)

            # Progress
            self.display(t,x)

        return x

    #----------------------------------------------------------
    # Secant Method
    # Info (En): https://en.wikipedia.org/wiki/Secant_method
    # Info (Ch): https://zh.wikipedia.org/wiki/割线法
    #----------------------------------------------------------
    def secant(self):
        self.err = []
        x = self.x1

        for t in range(self.T):
            # Algorithm
            prev = x
            fx0  = self.f(self.x0)
            fx1  = self.f(self.x1)
            x    = self.x1 - fx1 * (self.x1 - self.x0) / (fx1 - fx0 + self.eps)
            self.x0 = self.x1
            self.x1 = x

            # Loss
            error = abs(prev - x)
            self.err.append(error)

            # Progress
            self.display(t,x)

        return x

    #----------------------------------------------------------
    # Newton-Raphson Method
    # Info (En): https://en.wikipedia.org/wiki/Newton%27s_method
    # Info (Ch): https://zh.wikipedia.org/wiki/牛顿法
    #----------------------------------------------------------
    def newton(self):
        x = self.x0

        for t in range(self.T):
            # Algorithm
            prev = x
            x = x - self.f(x)/(self.df(x) + self.eps)

            # Loss
            error = abs(prev - x)
            self.err.append(error)

            # Progress
            self.display(t,x)

        return x

    #----------------------------------------------------------
    # Halley’s Method
    # Info (En): https://en.wikipedia.org/wiki/Halley%27s_method
    #----------------------------------------------------------
    def halley(self):
        x = self.x0

        for t in range(self.T):
            # Algorithm
            prev = x
            fx = self.f(x)
            dfx = self.df(x)
            ddfx = self.ddf(x)
            x = x - 2*fx*dfx / ( (2*(dfx**2) - fx*ddfx) + self.eps)

            # Loss
            error = abs(prev - x)
            self.err.append(error)

            # Progress
            self.display(t,x)

        return x
