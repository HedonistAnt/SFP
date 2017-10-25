import matplotlib.pyplot as plt
from math import sin,cos,sqrt,asin,pi
from numpy import arange,vectorize
from scipy.optimize import brenth,minimize_scalar

def aproximate_theta(Rho):
    n=2
    aa = (n - 1 / n) ** 2 + Rho * (n + 1 / n) ** 2
    bb = 4 * Rho * (n ** 2 + 1) * (aa - 4 * Rho)
    cc = bb ** 2 + 16 * (Rho) ** 2 * (16 * (Rho) ** 2 - aa ** 2) * (n ** 2 - 1) ** 2
    dd = ((-bb - cc ** (1 / 2)) / (2 * (16 * (Rho) ** 2 - aa ** 2))) ** (1 / 2)
    try:
        theta = asin(dd)
    except:
        theta=0
        print("complex")
    return  theta
def main():
    n=2
    f_rho=lambda theta: ((n - 1 / n) ** 2 )* ((sin(theta)) ** 2 )/ (
                2 + 2 * (n ** 2) - ((n + 1 / n) ** 2) * (sin(theta)) ** 2 + 4 * cos(theta) * sqrt(
                    n ** 2 - (sin(theta)) ** 2))
    arrho=list(arange(0,0.99,0.01))
    apr_theta = list(map(lambda Rho: aproximate_theta(float(Rho)),arrho))

    newrho=list(map(f_rho,apr_theta))

    error = [abs(a-b) for (a,b) in zip(arrho,newrho)]
    print(error)
    plt.plot(arrho,error)
    plt.xlabel("rho")
    plt.ylabel("error of theta aproximation")
    plt.grid(True)
    plt.show()
if __name__=="__main__":
      main()