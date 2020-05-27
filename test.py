'''
 *  Author : Bao Jiarong
 *  Contact: bao.salirong@gmail.com
 *
 *  Created  On: 2020-05-27
 *  Modified On: 2020-05-27
 '''
import src.na as numb

def h(x):
    return (x-4)**2-4

def dh(x):
    return 2*x-12

def ddh(x):
    return 2

na = numb.NA(a  =-10,    # Search domain
             b  = 10,    # Search domain
             T  =100,    # Maximum number of iterations
             f  =  h,    # The function to solve
             df = dh,
             ddf=ddh)

#----------------------------na------------------------------
print("Bisection")
x = na.bisection()
print("x =",x,"h(x) =",h(x))

#--------------
print("Secant")
x = na.secant()
print("x =",x,"h(x) =",h(x))

#--------------
print("Newton")
x = na.newton()
print("x =",x,"h(x) =",h(x))

#--------------
print("Halley")
x = na.halley()
print("x =",x,"h(x) =",h(x))

# na.plot()
