# CSE202 - Design and Algorithms Analysis
# Midterm 2020
# Author: Yubo Cai

import math
import hashlib


def bin_hash(x):
    hash_object = hashlib.sha1(str(x).encode('utf-8'))
    hexa = hash_object.hexdigest()
    bina = bin(int(hexa, 16))[2:].zfill(160)[:32]
    return bina


### CODE TO BE COMPLETED


# Question 1
def cardinality(tab):
    table = {}
    for el in tab:
        if el not in table:
            table[el] = 1
    return len(table)


# Question 2
def bucket(bina, b):
    # returns the integer corresponding to the leftmost b bits in bina
    return int(bina[:b], 2)


def zeros(bina, b):
    # return the largest l, called b-length of bina, such that all entries in bina[b:b+l] are zeros
    if len(bina) == 0:
        return None
    l = 0
    n = len(bina)
    while b + l < n and bina[b + l] == '0':
        l += 1
    return l


# Question 3
def sketch(L, b):
    # returns the array A of length 2**b, such that A[i] is 0 if the bucket of index i is empty,
    # and otherwise A[i] is one plus the maximum value taken by the b-length over all elements in the bucket of index i
    res = [0] * 2**b
    for x in L:
        bina = bin_hash(x)
        i = bucket(bina, b)
        res[i] = max(res[i], 1 + zeros(
            bina, b))  # 如果在index i上面没有值，则直接为0，否则返回所有在bucket上的最大值的1+zero value
    return res


def constant(b):
    # function to compute the constant alpha(b), given
    if b == 4: return 0.673
    elif b == 5: return 0.697
    elif b == 6: return 0.709
    else: return 0.7213 / (1 + 1.079 / 2**b)


# Question 4
def loglog(L, b):
    const = constant(b)
    m = 2**b
    sum_m = 0
    sket = sketch(L, b)
    for i in range(m):
        sum_m += 1 / 2**sket[i]
    return const * m**2 / sum_m


# Question 5
def loglog_small_range_correction(L, b):
    m = 2**b
    E = loglog(L, b)
    V = 0
    if E <= (5 * m / 2):
        lis = sketch(L, b)
        for i in range(m):
            if lis[i] == 0:
                V += 1
        if V == 0:
            return E
        else:
            return m * math.log(m / V)
    else:
        return E
