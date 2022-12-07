#!/usr/bin/env sage

import sys
import math
from sage.all import *
import numpy as np
import Prime as p


# defining RSA as a trapdoor function

# defines RSA
class Rsa:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q

    def fpk(self, pk, m):
        return pow(m, pk[0], self.n)

    def fsk(self, sk, c):
        return pow(c, sk[0], self.n)

    def keygen(self, n):
        pk = math.randint(1,n-1)
        phi_n = ((self.p - 1) * (self.q-1))
        while math.gcd(pk, phi_n) != 1:
            pk = math.randint(1, n-1)
        sk = sage.inverse_mod(pk, phi_n)
        return (pk, n), (sk, n)


class Encryption:
    def __init__(self, key_rsa, key_hash):
        self.pk = key_rsa[0]
        self.sk = key_rsa[1]
        self.k = key_hash
        self.rsa = None
        self.hash = None

    def keyGen(self):
        p = random_prime()
        q = random_prime()
        while p == q:
            q = random_prime()
        self.rsa = Rsa()

# getRandomPrime(primeType,totalDigits,mode=0)