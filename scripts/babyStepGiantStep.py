#!/usr/bin/env sage

import sys
import math
from sage.all import *

def baby_step_giant_step(g1, g2, order, h1, h2, p):
    l = math.floor(math.sqrt(order))
    list_g1 = [1, g1]
    list_g2 = [1, g2]
    for i in range(2, l + 1):
        result = exponent_function(g1, g2, i, p)
        list_g1.append(result[0])
        list_g2.append(result[1])
    # compute g^-l so i can compute (g^-l)^j mod p
    for j in range(2, l + 2):



def exponent_function(g1, g2, exp, p):
    list_g1 = [1, g1]
    list_g2 = [1, g2]

    for i in range(2, exp + 1):
        new_g1 = (list_g1[i - 1] * list_g1[i - 1] + (3 * list_g2[i-1] * list_g2[i-1])) % p
        new_g2 = (2 * list_g1[i-1] * list_g2[i-1]) % p
        list_g1.append(new_g1)
        list_g2.append(new_g2)

    return list_g1[exp], list_g2[exp]

baby_step_giant_step(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))