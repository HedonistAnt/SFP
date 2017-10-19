from PIL import Image
import solvingsystem
import math
import numpy as np
import sympy

def minimize(f,df,rho):
    dim = 1.
    dimp=100000
    while abs(dimp-dim)>0.001:
        dim = dim - float(f(dim,rho))/float(df(dim))
        dimp=dim

    return dim

def main():
    img0=Image.open(".\\photo\\IMG0.png").convert('L')
    img45=Image.open(".\\photo\\IMG45.png").convert('L')
    img90=Image.open(".\\photo\\IMG90.png").convert('L')

    width,height=img0.size

    map = Image.new("L", (width,height), (0))

    Phi= np.zeros((width,height))
    Rho=np.zeros((width,height))
    Theta = np.zeros((width,height))
    n = 0.1
    theta=sympy.symbols("theta")
    rho=sympy.symbols("rho")
    f = 2*n*sympy.tan(theta)*sympy.sin(theta)/((sympy.tan(theta))**2*(sympy.sin(theta))**2 + n**2) - rho
    print(f)
    df=sympy.diff(f,theta)
    df=sympy.lambdify(theta,df)
    f=sympy.lambdify((theta,rho),f)

    for x in range(width):
        for y in range(height):
          Imax,Imin,Phi[x,y]=solvingsystem.solve_system([img0.getpixel((x,y)),img45.getpixel((x,y)),img90.getpixel((x,y))])
          Rho=(Imax-Imin)/(Imax+Imin)
          Theta[x,y]=minimize(f,df,Rho)
          map.putpixel((x,y),abs(math.floor(255*Theta[x,y]/2)))
          map.save(".\\maps\\thetamap.png", "PNG")
          print(abs(math.floor(255*Theta[x,y]/2)))
    map.save(".\\maps\\thetamap.png", "PNG")

if __name__=="__main__":



    main()