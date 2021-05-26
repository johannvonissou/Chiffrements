#!/bin/python3

from secrets import randbelow
import base64

class RSA:
    def generation_cles(self):
        p, q = self.__selection_premiers()
        n = p * q
        phi = (q-1)*(p-1)
        e = self.__pub_cle(phi)
        d = self.__pri_cle(e, phi)
        self.__clepub = (n, e)
        self.__clepri = (n, d)
        return ((n, e), (n, d))

    def get_clepub(self):
        return self.__clepub

    def get_clepri(self):
        return self.__clepri

    def set_clepub(self, cle):
        self.__clepub = cle

    def set_clepri(self, cle):
        self.__clepri = cle

    def __pgcd(self, a, b):
        if a < b:
            (a, b) = (b, a)
        if a % b == 0:
            return b
        else:
            return self.__pgcd(b, a % b)

    def __pgcde(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__pgcde(b % a, a)
            return (g, x - (b // a) * y, y)

    def __inverse_modulaire(self, a, m):
        g, x, y = self.__pgcde(a, m)
        if g != 1:
            raise Exception("Inverse modulaire inexistant.")
        else:
            return x % m

    def __pub_cle(self, phi):
        while True:
            e = randbelow(phi)
            if e <= 2 or e >= phi:
                continue
            if self.__pgcd(e, phi) == 1:
                return e

    def __pri_cle(self, e, phi):
        return self.__inverse_modulaire(e, phi)

    def __selection_premiers(self):
        with open("primes.txt", 'r') as f:
            np = f.readlines()
        p, q = -1, -1
        while p == -1 or q == -1 or p == q:
            p = randbelow(len(np))
            q = randbelow(len(np))
        return int(np[p]), int(np[q])

    def __bits(self, m):
        n = int(m)
        while n:
            yield n & 1
            n >>= 1
 
    def __exp_rapide(self, x, n):
        r = 1
        p = x
    
        for bit in self.__bits(n):
            if bit: r *= p
            p **= 2
        return r

    def calcul_nombre(self, n, cle):
        if n >= 0 and n < cle[0]:
            return self.__exp_rapide(n, cle[1]) % cle[0]
        else:
            raise Exception("La taille spécifié est invalide ! ({}>{})".format(n, cle[0]))

    def chiffrer_chaine(self, chaine):
        cchaine = str()
        for c in chaine:
            cchaine += str(self.calcul_nombre(ord(c), self.__clepub)) + ";"
        return base64.b64encode(cchaine.encode('utf-8')).decode('utf-8')

    def dechiffrer_chaine(self, cchaine):
        chaine = str()
        for c in base64.b64decode(cchaine.encode('utf-8')).decode('utf-8').split(";"):
            if(c == ""): continue
            chaine += chr(self.calcul_nombre(int(c), self.__clepri))
        return chaine

    def __init__(self, keygen=True):
        if keygen: self.generation_cles()
