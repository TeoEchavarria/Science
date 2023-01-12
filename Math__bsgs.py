# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:29:24 2022

@author: Mateo
"""

p =13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

g =11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

h =7878990714250916313123685004297703453554975760393326511084655856181862437620849483031663369571911243139599217011568427686722396876497863525857863056968479

from math import ceil, sqrt


def baby_step_giant_step(g, h, p):
    '''
    Resolver h = g^x mod p.
    '''
    N = 33554432

    # Diccionario g^{1...m} (mod p).
    DB = {pow(g, i, p): i for i in range(N)}

    c = pow(g, N * (p - 2), p)

    # Buscar el equivalente en DB.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in DB:
            return j * N + DB[y]

    # Solution not found
    return None


print(baby_step_giant_step(g, h, p))

        
    