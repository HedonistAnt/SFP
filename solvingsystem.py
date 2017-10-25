from math import pi, tan, sqrt, sin, cos


def solve_system(I):
    i1, i2, i3 = I[0], I[1], I[2]
    if abs(i1 ** 2 - 2 * i3 * i1 - sqrt(i1 ** 2 - 2 * i3 * i1 + i3 ** 2 + 4) * i1 + i3 ** 2 + i3 * sqrt(
                                            i1 ** 2 - 2 * i1 * i3 + i3 ** 2 + 4) + 4) > 0.001:
        phi_value = tan(0.5 * (i1 - i3 - sqrt((i3 - i1) ** 2 + 4)))
    else:
        phi_value = tan(0.5 * (i1 - i3 + sqrt((i3 - i1) ** 2 + 4)))


    while(phi_value>pi):
        phi_value-=pi

    while (phi_value < 0.0):
        phi_value += pi

    imin_value = ((i1 + i3) * (1 + sin(2 * phi_value)) - 2 * i2) / (2 * sin(2 * phi_value))
    imax_value = i1 + i3 - ((i1 + i3) * (1 + sin(2 * phi_value)) - 2 * i2) / (2 * sin(2 * phi_value))

    return imax_value, imin_value, phi_value


if __name__ == "__main__":
    solve_system([185, 112, 78])
