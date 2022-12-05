#!/usr/bin/env sage

import sys
import math
from sage.all import *
def multiply_function(m1, m2, p):
    alpha = ((m1[0] * m2[0]) + (3 * m1[1] * m2[1])) % p
    beta = ((m2[0] * m1[1]) + (m1[0] * m2[1])) % p
    return alpha,beta


def baby_step_giant_step(g1, g2, order, h1, h2, p):
    l = math.floor(math.sqrt(order))
    list_baby = [(1,1),(g1,g2)]
    for i in range(2, l + 1):
        list_baby.append(exponent_function(g1, g2, i, p))

    #computed these in sage then hardcoded them in
    inv_g1 = 105
    inv_g2 = 62

    index_1 = 0
    index_2 = 0
    first_giant = multiply_function((h1 , h2) , (inv_g1 , inv_g2), 127)
    list_giant = [(h1,h2), first_giant]
    match_found = False
    multiplier = (h1, h2)
    for j in range(2, l + 2):
        exponentiation = exponent_function(inv_g1, inv_g2, j, p)
        list_giant.append(multiply_function(exponentiation, multiplier, p))
        for k in range(len(list_baby)):
            if list_baby[k] in list_giant:
                index_1 = k
                index_2 = list_giant.index(list_baby[k])
                match_found = True
                break
        if match_found:
            break

    a = (index_1 + (l * index_2)) % order
    print("our a is: " + str(a))
    check = exponent_function(g1, g2, a, p)
    if check[0] == h1 and check[1] == h2:
        print("answer validated")
    else:
        print("something went wrong, answer incorrect")
        print("our g^a is: " + str(check))

    print("our indexes were:- a_0: " + str(index_1) + "  a_1: " + str(index_2))
def exponent_function(g1, g2, exp, p):
    curr_g1 = g1
    curr_g2 = g2
    for i in range(2, exp + 1):
        curr_g1, curr_g2 = multiply_function((g1 , g2), (curr_g1, curr_g2), p)

    return curr_g1, curr_g2


baby_step_giant_step(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
# print("g^l is:- " + str(exponent_function(125, 18, 126, 127)))

