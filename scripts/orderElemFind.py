#!/usr/bin/env sage

import sys
from sage.all import *

# Function that takes in an order and the size of a finite field.
# Returns an element if it exists of the required order, or 0 otherwise.
def find_elem_order(order, size):
    elem = 0
    field = GF(1031).unit_group()
    for i in range(2, size):
        if field[i].multiplicative_order() == order:
            elem = i
            break
    print(elem)


find_elem_order(int(sys.argv[1]), int(sys.argv[2]))