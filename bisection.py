import numpy as np


def bi_section(f, a, b):
    '''
    This is a function that calculates a root for given function "f"
    in the interval [a, b]
    inputs:
    f : the function for which we calculate the root
    a : the beginning of the interval
    b : the end of interval
    '''

    # the main while loop to check
    # if we are close enough to the desired tolerance
    while abs(b-a) > 1e-8:
        # we have chosen the tolerance to be 1e-8 but we can consider
        # to give it as a parameter to the function
        c = (a+b)/2  # derive the mid point
        if f(a)*f(c) < 0:
            b = c
        elif f(b)*f(c) < 0:
            a = c
        # catch the cases where the end of intervals or mid point
        # the exact root
        elif f(a) == 0:
            return a
        elif f(b) == 0:
            return b
        elif f(c) == 0:
            return c

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
