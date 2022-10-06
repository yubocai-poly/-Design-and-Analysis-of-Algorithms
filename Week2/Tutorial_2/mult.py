# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-9-29

# Q1


def poly_mult(P, Q):
    len_p = len(P)
    len_q = len(Q)
    result = [0] * (len_p + len_q - 1)
    for i in range(len_p):
        for j in range(len_q):
            result[i + j] += P[i] * Q[j]
    return result


def cost_poly_mult(n):
    return 2 * n**2 - 2 * n + 1


# Q2


def poly_add(P, Q):
    len_p = len(P)
    len_q = len(Q)
    result = [0] * max(len_p, len_q)
    for i in range(len_p):
        result[i] += P[i]
    for j in range(len_q):
        result[j] += Q[j]
    return result


def neg(P):
    return [-x for x in P]


def shift(P, k):
    return [0] * k + P


# Q3


def poly_kara_mult(P, Q):
    # Here we assume that P and Q have the same length
    # We apply the Karatsuba algorithm to P and Q
    assert len(P) == len(
        Q
    ), "this method only works when P and Q have the same number of coefficients"
    length = len(P)
    if length == 1:
        return [P[0] * Q[0]]
    k = length // 2
    P0 = P[:k]
    P1 = P[k:]
    Q0 = Q[:k]
    Q1 = Q[k:]
    H0 = poly_kara_mult(P0, Q0)
    H2 = poly_kara_mult(P1, Q1)
    H1 = poly_kara_mult(poly_add(P0, P1), poly_add(Q0, Q1))
    mid = poly_add(poly_add(H1, neg(H0)), neg(H2))
    return poly_add(poly_add(H0, shift(mid, k)), shift(H2, 2 * k))


def cost_poly_kara_mult(n):
    if n == 1:
        return 1
    return 3 * cost_poly_kara_mult((n + 1) // 2) + 4 * n


# Q4


def cost_poly_tc3_mult(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n % 3 == 0:
        return 5 * cost_poly_tc3_mult(n // 3) + 30 * n
    if n % 3 == 1:
        return 5 * cost_poly_tc3_mult((n + 2) // 3) + 30 * n
    if n % 3 == 2:
        return 5 * cost_poly_tc3_mult((n + 1) // 3) + 30 * n


# Q5 hybrid


def poly_switch_mult(d, P, Q):
    # Here we assume that P and Q have the same length
    assert len(P) == len(
        Q
    ), "this method only works when P and Q have the same number of coefficients"
    n = len(P)
    if n <= d:
        return poly_mult(P, Q)
    k = n // 2
    P0 = P[:k]
    P1 = P[k:]
    Q0 = Q[:k]
    Q1 = Q[k:]
    H0 = poly_switch_mult(d, P0, Q0)
    H2 = poly_switch_mult(d, P1, Q1)
    H1 = poly_switch_mult(d, poly_add(P0, P1), poly_add(Q0, Q1))
    mid = poly_add(poly_add(H1, neg(H0)), neg(H2))
    return poly_add(poly_add(H0, shift(mid, k)), shift(H2, 2 * k))


def cost_switch_mult(d, n):
    if n <= d:
        return 2 * n**2 - 2 * n + 1
    return 3 * cost_switch_mult(d, (n + 1) // 2) + 4 * n


for d in range(1, 100, 10):
    print(cost_switch_mult(d, 50))

"""
We find that when d = 1, the cost is the largest, which means we use the karatsuba algorithm for all the computation.
However, we we increase d = 10, some simple computation we just use the naive algorithm, which is much faster than use all in karatsuba.
after d > n, the cost remain the same since we only use the naive algorithm.
"""