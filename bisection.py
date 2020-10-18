import numpy as np

def bi_section(f, a, b, tol=1e-8):
    '''
    This is a function that calculates a root for given function "f"
    in the interval [a, b]

    Inputs:
    f : the function for which we calculate the root
    a : the beginning of the interval
    b : the end of interval
    '''

    # if any of the endpoints is an exact root, return it
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b

    # the main while loop to check
    # if we are close enough to the desired tolerance
    # we have chosen the tolerance to be 1e-8 but we can consider
    # to give it as a parameter to the function
    while abs(b-a) > tol:

        c = (a+b)/2  # derive the mid point

        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


def f(x):
    '''
    the function for which we are calculating the root
    '''
    y = np.cos(x)
    return y


a = 0
b = np.pi
print(np.pi/2)
print(bi_section(f, a, b))
