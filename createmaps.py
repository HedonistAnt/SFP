from PIL import Image
import solvingsystem
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math
import cv2
from mpmath.calculus.optimization import Newton


def minimize(f, df, r):
    x0 = 1
    for i in range (20):
        f_new = f(x0) - r

        x1 = x0 - f_new / df(x0)
        if abs(x1 - x0) < 0.001:
            return x1
        x0 = x1
    return 0


def main():
    phi = symbols('phi')


    img0 = cv2.imread(".\\photo\\IMG0.png", cv2.IMREAD_GRAYSCALE)
    img0 = np.array(img0)

    img45 = cv2.imread(".\\photo\\IMG45.png", cv2.IMREAD_GRAYSCALE)
    img45 = np.array(img45)

    img90 = cv2.imread(".\\photo\\IMG90.png", cv2.IMREAD_GRAYSCALE)
    img90 = np.array(img90)

    height, width = img0.shape
    map = np.zeros([height, width, 3], dtype=np.uint8)
    map = cv2.cvtColor(map, cv2.COLOR_RGB2GRAY)
    map = np.array(map)

    Theta = np.zeros((height, width))

    n = 1.6



    df = lambda theta: 4 * n ** 2 * (n ** 2 - 1) ** 2 * (
    n ** 2 * sqrt(n ** 2 - math.sin(theta) ** 2) * math.cos(theta) - n ** 2 * math.sin(theta) ** 2 + 2 * n ** 2 + sqrt(
        n ** 2 - math.sin(theta) ** 2) * math.cos(theta) - math.sin(theta) ** 2) * math.sin(theta) / (
                       sqrt(n ** 2 - math.sin(theta) ** 2) * (
                       2 * n ** 2 * (n ** 2 + 2 * sqrt(n ** 2 - math.sin(theta) ** 2) * math.cos(theta) + 1) - (
                       n ** 2 + 1) ** 2 * math.sin(theta) ** 2) ** 2)

    f = lambda theta: (n - 1 / n) ** 2 * (math.sin(theta)) ** 2 / (
        2 + 2 * n ** 2 - (n + 1 / n) ** 2 * (math.sin(theta)) ** 2 + 4 * math.cos(theta) * sqrt(
            n ** 2 - (math.sin(theta)) ** 2))

    for x in range(height):
        for y in range(width):
            Imax, Imin, Phi = solvingsystem.solve_system([img0.item((x, y)), img45.item((x, y)), img90.item((x, y))])

            Rho = (Imax - Imin) / (Imax + Imin)
            print(Rho)
            Theta[x, y] = minimize(f, df, Rho)
            map[x, y] = abs(math.floor(255 * Theta.item((x, y))/2))

    map = np.asarray(map)

    cv2.imwrite(".\\maps\\thetamap.png", map)


if __name__ == "__main__":
    main()
