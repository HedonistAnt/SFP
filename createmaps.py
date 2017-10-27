
import solvingsystem

import numpy as np
import matplotlib.pyplot as plt

from math import sin,cos,sqrt,floor,asin,pi
import cv2
from scipy.optimize import minimize_scalar,minimize,bisect

def findtheta (rho,n,Imax,Imin,i1,i2,i3):
    if rho<0:
        return -2
    f_rho = lambda theta: ((n - 1 / n) ** 2) * ((sin(theta)) ** 2) / (
        2 + 2 * (n ** 2) - ((n + 1 / n) ** 2) * (sin(theta)) ** 2 + 4 * cos(theta) * sqrt(
            n ** 2 - (sin(theta)) ** 2))-rho
    nf_rho = lambda theta: -(((n - 1 / n) ** 2) * ((sin(theta)) ** 2) / (
        2 + 2 * (n ** 2) - ((n + 1 / n) ** 2) * (sin(theta)) ** 2 + 4 * cos(theta) * sqrt(
            n ** 2 - (sin(theta)) ** 2)) - rho)
    try:
        Theta=bisect(f_rho,0,abs(minimize_scalar(nf_rho).x))
    except:
        Theta=-2
    return Theta





def main():



    img0 = cv2.imread("./photo/IMG0.png", cv2.IMREAD_GRAYSCALE)
    img0 = np.array(img0)

    img45 = cv2.imread("./photo/IMG45.png", cv2.IMREAD_GRAYSCALE)
    img45 = np.array(img45)

    img90 = cv2.imread("./photo/IMG90.png", cv2.IMREAD_GRAYSCALE)
    img90 = np.array(img90)

    height, width = img0.shape
    map = np.zeros([height, width, 3], dtype=np.uint8)
    map = cv2.cvtColor(map, cv2.COLOR_RGB2GRAY)
    map = np.array(map)

    cmap = np.zeros([height, width, 3], dtype=np.uint8)
    cmap = cv2.cvtColor(cmap, cv2.COLOR_RGB2GRAY)
    cmap = np.array(cmap)
    n = 1.4

    maxrho=0

    Phi=np.zeros((height,width))
    Theta = np.zeros((height, width))

    for x in range(height):
        for y in range(width):
            Imax, Imin, Phi[x,y] = solvingsystem.solve_system([img0.item((x, y)), img45.item((x, y)), img90.item((x, y))])
            Rho = (Imax - Imin) / (Imax + Imin)
            Theta[x,y]=findtheta(Rho,n,Imax,Imin,img0.item((x, y)), img45.item((x, y)), img90.item((x, y)))
            Theta[x,y]/=2
            map[x, y] = abs(floor(255 * Theta[x,y]))


    map = np.asarray(map)
    cmap=np.asarray(cmap)
    cv2.imwrite("./maps/thetamap.png", map)
    cv2.imwrite("./maps/cmap.png",cmap)

    plt.imshow(Theta,cmap='viridis')
    plt.colorbar(ticks=[Theta.min(),0,Theta.max()])
    plt.show()

    plt.imshow(Phi,cmap="RdBu")
    plt.colorbar(ticks=[Phi.min(), 0, Phi.max()])
    plt.show()
if __name__ == "__main__":
    main()
