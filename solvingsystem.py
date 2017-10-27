from math import pi, tan, sqrt, sin, cos,atan2
import numpy as np

def solve_system(I):
    i1, i2, i3 = I[0], I[1], I[2]

    I = np.matrix([[2*i1],[2*i2],[2*i3]])
    M = np.matrix([[1,1,0],[1,0,1],[1,-1,0]]).I
    a,b,c = M.dot(I)
    a,b,c=float(a),float(b),float(c)
    phi_value = atan2(c,b)/2
    try:

        imax_value=(a+c/sin(2*phi_value))/2
        imin_value = a - imax_value
    except:
        imax_value=(a+b/cos(2*phi_value))/2
        imin_value=a-imax_value



    return imax_value, imin_value, phi_value


if __name__ == "__main__":
    print(solve_system([175 ,176, 175]))
