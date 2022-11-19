#!/usr/bin/env sage

import sys
from sage.all import *

# Function that takes in values, gamma, h ,p and the order of gamma.
# returns b,c,b',c' to satisfy the equation (b' - b /c - c') = a mod order
# returns the a that satisfies the equation and verifies that the answer is correct.

def pollard_rho(gamma, h, p, order):
    # initialize list for each member of the triple.
    g = [gamma]
    b = [1]
    c = [0]

    terminate = False
    first_index = 0
    last_index = 0
    # iterate through a lot of values implementing the rules of pollard-rho. Terminate if we get
    # g_i = g_j for i != j.
    for i in range(1, p):
        if g[i-1] % 3 == 0:
            new_g = (g[i-1] * gamma) % p
            new_b = (b[i-1] + 1) % order
            if new_g in g:
                terminate = True
                first_index = g.index(new_g)
                last_index = i
            g.append(new_g)
            b.append(new_b)
            c.append(c[i-1])
        elif g[i-1] % 3 == 1:
            new_g = (g[i-1] * h) % p
            new_c = (c[i-1] + 1) % order
            if new_g in g:
                terminate = True
                first_index = g.index(new_g)
                last_index = i
            g.append(new_g)
            b.append(b[i-1])
            c.append(new_c)
        else:
            new_g = (g[i-1] * g[i-1]) % p
            new_b = (b[i-1] * 2) % order
            new_c = (c[i-1] * 2) % order
            if new_g in g:
                terminate = True
                first_index = g.index(new_g)
                last_index = i
            g.append(new_g)
            b.append(new_b)
            c.append(new_c)
        if terminate:
            print("G" + str(first_index) + " is the same as G" + str(last_index))
            break
    print("b' = " + str(b[last_index]))
    print("b = " + str(b[first_index]))
    print("c = " + str(c[first_index]))
    print("c' = " + str(c[last_index]))

    # a bit of wizardry since mathematical operators work differently in python rather than
    # just pure SageMath
    numerator = b[last_index] - b[first_index]
    denominator = c[first_index] - c[last_index]
    intermediate = 0
    if denominator < 0:
        denominator = inverse_mod(denominator, order)
        intermediate = numerator * denominator
    else:
        intermediate = numerator / denominator
    if intermediate < 0:
        intermediate = intermediate + order
    a = (intermediate % order)

    if pow(gamma, a, p) == h:
        print("verified that a satisfies equation.")
    else:
        print("somethings gone wrong and our a is incorrect.")

    print("a is " + str(a))
pollard_rho(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
