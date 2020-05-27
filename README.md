## Numerical Analysis in Python
The implemented numerical analysis are:

* Bisection,
* Secant,
* Newton,
* Halley.

All of the implemented algorithms can be used to find the minimum of 2D function.
For example : f(x) = (x-2)^2.

### Requirement
```
python==3.7.0
numpy==1.18.1
```
### How to use

Open test.py you will find some examples
```
import src.na as numb

def h(x):
    return (x-4)**2-4

def dh(x):
    return 2*x-12

def ddh(x):
    return 2

na = numb.NA(a=-10,
             b=10,
             T=100,
             f=h,
             df=dh,
             ddf=ddh)

x = na.bisection()
print("x =",x,"h(x) =",h(x))
```
