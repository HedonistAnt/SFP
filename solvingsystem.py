from sympy import sin, cos, diff,symbols,lambdify



def minimize(f,df):
    dim = 1.
    dimp=100000
    while abs(dimp-dim)>0.001:
        dim = dim - float(f(dim))/float(df(dim))
        dimp=dim

    return dim

def solve_system (I):
    i1,i2,i3=I[0],I[1],I[2]
    phi = symbols('phi')
    f=(i1+i3)/2 + ((i1+i3)/2 - (i1+i3)*(1+2*sin(2*phi))/2 + i2)*cos(2*phi) - i1
    df = diff(f,phi)
    f = lambdify(phi,f)
    df = lambdify(phi,df)
    phi_value=minimize(f,df)
    imin_value = (i1+i3)*(1+sin(2*phi_value))/2 - i2
    imax_value= i1+i3-imin_value
    return imax_value,imin_value,phi_value




if __name__=="__main__":

    phi = symbols('phi')
    i = symbols('i')


    print(solve_system([170,169,169]))


