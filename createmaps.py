
import solvingsystem

import numpy as np


from math import sin,cos,sqrt,floor,asin,pi
import cv2
from scipy.optimize import minimize_scalar,minimize





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



    for x in range(height):
        for y in range(width):
            Imax, Imin, Phi = solvingsystem.solve_system([img0.item((x, y)), img45.item((x, y)), img90.item((x, y))])

            Rho = (Imax - Imin) / (Imax + Imin)



            print(Phi)

            aa = (n - 1 / n)** 2 + Rho * (n + 1/ n) **2
            bb = 4 * Rho * (n ** 2 + 1) * (aa - 4 * Rho)
            cc = bb ** 2 + 16 * (Rho) ** 2 * (16 * (Rho) ** 2 - aa **2) * (n **2 - 1) **2
            dd = ((-bb - cc **(1 / 2)) / (2 * (16 * (Rho) **2 - aa **2))) **(1 / 2)
            try:
                theta = asin(dd)

            except:
                cmap[x,y]=255
                theta=0

            while(theta<0.0):
                theta += 2*pi
                print("lol")

            while(theta>2.):
                theta-=2*pi


            theta/=2


            map[x, y] = abs(floor(255 * theta))


    map = np.asarray(map)
    cmap=np.asarray(cmap)
    cv2.imwrite("./maps/thetamap.png", map)
    cv2.imwrite("./maps/cmap.png",cmap)

if __name__ == "__main__":
    main()
