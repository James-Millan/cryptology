#!/usr/bin/env sage

import sys
import math
from sage.all import *
import numpy as np


def calculate_inverse(g1, g2, p, l):
    new_g1, new_g2 = exponent_function(g1, g2, l, p)

    # solve simultaneous equations
    x1 = new_g1
    x2 = 3 * new_g2
    x3 = new_g2
    x4 = new_g1

    a = [[x1,x2],[x3,x4]]
    b = [1, 0]

    result = np.linalg.solve(a, b)
    # a is supposed to be 1/13 but due to how floats are stored its incorrect. Therefore I have had to calculate
    # the inverse
    # by hand for this question and hard code it for the numbers given in the question :(
    alpha_float = result[0].as_integer_ratio()
    beta_float = result[1].as_integer_ratio()
    print(result)
    print(alpha_float)
    print(beta_float)

    # sort them out into the correct form
    a_numerator = alpha_float[0] % p
    a_denominator = inverse_mod(alpha_float[1], p)
    alpha = (a_numerator * a_denominator) % p
    b_numerator = beta_float[0] % p
    b_denominator = inverse_mod(beta_float[1], p)
    beta = (b_numerator * b_denominator) % p

    # now multiply together an ensure we get the correct inverse
    multiplied_alpha = ((new_g1 * alpha) + (3 * beta * new_g2)) % p
    multiplied_beta = ((beta * new_g1) + (alpha * new_g2)) % p

    if multiplied_alpha == 1 and multiplied_beta == 0:
        print("inverse calculated correctly")
    else:
        print("inverse went wrong")
    print(new_g1, new_g2)
    print(alpha, beta)
    print(multiplied_alpha, multiplied_beta)

    return alpha, beta


def multiply_function(m1, m2, p):
    alpha = ((m1[0] * m2[0]) + (3 * m1[1] * m2[1])) % p
    beta = ((m2[0] * m1[1]) + (m1[0] * m2[1])) % p
    return alpha,beta


def baby_step_giant_step(g1, g2, order, h1, h2, p):
    l = math.floor(math.sqrt(order))
    list_baby = [(g1,g2)]
    for i in range(2, l + 1):
        list_baby.append(exponent_function(g1, g2, i, p))
    print("length of babylist " + str(len(list_baby)))
    print(list_baby)
    # compute g^-l so i can compute (g^-l)^j mod p which is (105 + 165 sqrt{3})^-1)
    inv_g1 = 34
    inv_g2 = 1
    index_1 = 0
    index_2 = 0
    list_giant = [(inv_g1, inv_g2)]
    match_found = False
    multiplier = [h1, h2]
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
    print("length of giant_list " + str(len(list_giant)))
    print(list_giant)
        # if result in list_baby and result in list_giant:
        #
        #       if list_baby.index(result) ==  list_giant.index(result):
        #         # return indexes of these.
        #         # print(result)
        #         # print(list_g1.index(result[0]), list_g2.index(result[1]))
        #         index_1 = list_baby.index(result[0])
        #         index_2 = j - 2
    a = (index_1 + 1 + (l * (index_2 + 1))) % order
    print("our a is: " + str(a))
    check = exponent_function(g1, g2, a, p)
    if check[0] == h1 and check[1] == h2:
        print("answer validated")
    else:
        print("something went wrong, answer incorrect")
        print("our g^a is: " + str(check))

    print("our indexes were:- " + str(index_1) + "   " + str(index_2))
    print(list_baby[index_1], list_giant[index_2])
    # print(a)
    # print(index_1, index_2)
    # print(list_b1[index_1], list_b2[index_2])
    # print(list_g1[index_1], list_g2[index_2])


def exponent_function(g1, g2, exp, p):
    # list_g1 = [1, g1]
    # list_g2 = [1, g2]

    curr_g1 = g1
    curr_g2 = g2
    for i in range(2, exp + 1):
        curr_g1, curr_g2 = multiply_function((g1,g2), (curr_g1, curr_g2), p)
        # new_g1 = ((list_g1[i - 1] * list_g1[1]) + (3 * list_g2[i-1] * list_g2[1])) % p
        # new_g2 = ((list_g1[i-1] * list_g2[1]) + (list_g2[i-1] * list_g1[1])) % p
        # list_g1.append(new_g1)
        # list_g2.append(new_g2)

    return curr_g1, curr_g2


baby_step_giant_step(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))


print(exponent_function(125, 18, 126,127))
#94 + 99 sqrt{3}
for i in range(20000):
     result = exponent_function(125, 18, i, 127)
     if result[0] == 37 and result[1] == 12:
          print(i, result)
          break

#print(multiply_function([105,165],[34,1],127))
#exponent_function(125, 18, 20, 127)

