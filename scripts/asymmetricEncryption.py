#!/usr/bin/env sage

import sys
import math
from sage.all import *
import hashlib
import random


# defining RSA as a trapdoor function

# defines RSA
class Rsa:
    def __init__(self, n):
        self.n = n

    def fpk(self, pk, m):
        return pow(m, pk[0], self.n)

    def fsk(self, sk, c):
        return pow(c, sk[0], self.n)

    def keygen(self, p, q):
        pk = random.randint(1, p * q)
        phi_n = ((p - 1) * (q-1))
        while math.gcd(pk, phi_n) != 1:
            pk = random.randint(1, p * q)
        sk = inverse_mod(pk, phi_n)
        return (pk, p * q), (sk, p * q)


class Encryption:
    def __init__(self):
        self.pk = (0, 0)
        self.sk = (0, 0)
        self.max_int = 4294967296
        self.rsa = None
        self.hash = None

    def key_gen(self):
        p = random_prime(self.max_int)
        q = random_prime(self.max_int)
        while p == q:
            q = random_prime(self.max_int)
        self.rsa = Rsa(p * q)
        self.hash = hashlib.sha256()
        return self.rsa.keygen(p, q)

    def encryption(self, m, public, n):
        self.hash = hashlib.sha256()
        self.rsa = Rsa(n)
        pk = (public, n)
        r = random.randint(1, self.rsa.n)
        self.hash.update(repr(r).encode())
        s = self.hash.hexdigest()
        f_of_r = self.rsa.fpk(pk, r)
        s_xor_m = xor(s, m)
        return f_of_r, s_xor_m

    def decryption(self, h, c, secret, n):
        self.hash = hashlib.sha256()
        self.rsa = Rsa(n)
        sk = (secret, n)
        r = self.rsa.fsk(sk, h)
        self.hash.update(repr(r).encode())
        s = self.hash.hexdigest()
        s_xor_c = xor(s, c)
        print(s_xor_c)
        return bytes.fromhex(s_xor_c).decode("ASCII")


def xor(string1, string2):
    shortest = ""
    longest = ""
    if len(string1) >= len(string2):
        longest = string1
        shortest = string2
    else:
        longest = string2
        shortest = string1

    result = []
    for i in range(len(shortest)):
            result.append(ord(longest[i]) ^ ord(shortest[i]))
    hex_string = ""
    for j in result:
        hex_string = hex_string + hex(j)[2:]
    return hex_string


def default_error_usage():
    print("correct usage: - \n")
    print("sage asymmetricEncryption.py -MODE [arguments] \n")
    print("run sage asymmetricEncryption.py -h \n")
    print("for more details.")


def help_message():
    print("my encryption scheme has the following commands: \n")
    print("sage asymmetricEncryption.py -k \n")
    print("returns two pairs. Your public key followed by your private key.\n")
    print("sage asymmetricEncryption.py -e [message] [public_key] [n] \n")
    print("where [message] is a 16 characters of ASCII encoded plaintext and [public_key] is the first element of the first "
          + "pair returned by keygen \n")
    print("[n] is the modulus for your public key, the second element of either pair returned by keygen. \n")
    print("the output is two pieces of information: the f_pk(r) and H(r) XOR m \n")
    print("sage asymmetricEncryption.py -d [h] [c] [sk] \n")
    print("where h is the first output of encryption. c is the second output of encryption and sk is your secret key \n")

arguments = sys.argv[1:]
argc = len(arguments)
if argc < 1 or argc > 5:
    default_error_usage()
elif argc == 1:
    if str(arguments[0]) == "-h":
        help_message()
    elif str(arguments[0]) == "-k":
        enc = Encryption()
        print(enc.key_gen())
    else:
        default_error_usage()
elif argc == 4:
    if str(arguments[0]) == "-e":
        m = arguments[1]
        pk = arguments[2]
        n = arguments[3]
        print(m)
        print(pk)
        print(n)
        enc = Encryption()
        print(enc.encryption(m, int(pk), int(n)))
    else:
        default_error_usage()
elif argc == 5:
    if str(arguments[0]) == "-d":
        h = arguments[1]
        c = arguments[2]
        sk = arguments[3]
        n = arguments[4]
        enc = Encryption()
        print(enc.decryption(int(h), c, int(sk), int(n)))
    else:
        default_error_usage()
else:
    default_error_usage()

######TESTS######
enc = Encryption()
pk, sk = enc.key_gen()
m = "abcdefghijklmnop"
e = enc.encryption(m,pk[0],pk[1])
enc.decryption(e[0], e[1], sk[0], sk[1])