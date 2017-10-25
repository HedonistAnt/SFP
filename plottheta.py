import matplotlib.pyplot as plt
from math import sin,cos,sqrt,asin,pi
from numpy import arange,vectorize
from scipy.optimize import brenth,minimize_scalar

Rho=0.2
n=1.4
f = lambda theta: ((n - 1 / n) ** 2 )* ((sin(theta)) ** 2 )/ (
                2 + 2 * (n ** 2) - ((n + 1 / n) ** 2) * (sin(theta)) ** 2 + 4 * cos(theta) * sqrt(
                    n ** 2 - (sin(theta)) ** 2))-Rho
f_=lambda theta: -((n - 1 / n) ** 2 )* ((sin(theta)) ** 2 )/ (
                2 + 2 * (n ** 2) - ((n + 1 / n) ** 2) * (sin(theta)) ** 2 + 4 * cos(theta) * sqrt(
                    n ** 2 - (sin(theta)) ** 2))-Rho
a=0
b=minimize_scalar(f_).x
print("b=",b)
print(brenth(f,a,b,xtol=0.0001))
aa = (n - 1 / n)** 2 + Rho * (n + 1/ n) **2
bb = 4 * Rho * (n ** 2 + 1) * (aa - 4 * Rho)
cc = bb ** 2 + 16 * (Rho) ** 2 * (16 * (Rho) ** 2 - aa **2) * (n **2 - 1) **2
dd = ((-bb - cc **(1 / 2)) / (2 * (16 * (Rho) **2 - aa **2))) **(1 / 2)
try:
    theta = asin(dd)
    print(theta)

except:
    print("fail")

f2=vectorize(f)
plt.ylabel('f(theta)')
plt.xlabel('theta')
plt.grid(True)
t=arange(-5,5,0.001)
plt.plot(t,f2(t))

plt.show()