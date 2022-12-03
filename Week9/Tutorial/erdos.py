# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Yubo Cai

from uf import Rank_UF
import random
import math


# Analyzing the Erdős–Rényi model of random graph
# Question 3
def Erdos_Renyi(N):
    '''
    TO IMPLEMENT
    '''
    uf = Rank_UF(N)
    count = 0
    while uf.get_count() > 1:
        p, q = random.randint(0, N - 1), random.randint(0, N - 1)
        uf.union(p, q)
        count += 1

    return count