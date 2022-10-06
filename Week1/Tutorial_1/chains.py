# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-9-22

import math
from PowerTree import *


## Q1 ##
def bin_pow(x, n):  # check
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return bin_pow(x, n // 2) * bin_pow(x, n // 2)
    else:
        return bin_pow(x, n // 2) * bin_pow(x, n // 2) * x


## Q2 ##
def cost_bin_pow(n):  # check
    if n == 0 or n == 1:
        return 0

    if n % 2 == 0:
        return 1 + cost_bin_pow(n // 2)

    else:
        return 2 + cost_bin_pow(n // 2)


## Q3 ##
def smallest_factor(n):
    if n < 2:
        return -1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return -1


## Q4 ##
def factor_pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    p = smallest_factor(n)
    if p == -1:
        return x * factor_pow(x, n - 1)
    else:
        return factor_pow(factor_pow(x, p), n // p)


## Q5 ##
def cost_factor_pow(n):
    if n == 0 or n == 1:
        return 0

    p = smallest_factor(n)
    if p == -1:
        return 1 + cost_factor_pow(n - 1)
    else:
        return cost_factor_pow(p) + cost_factor_pow(n // p)


## Q6 ##
def power_from_chain(x, chain):
    # we use a dict to store the powers of x
    # we first initialize the dict with the first element of the chain
    # [1, 2, 3, 6, 12, 15] 是simple chain, [1, 2, 4, 6, 10, 14, 16, 24] 不是simple chain是因为24前面的16+y, 但是y不在前面的值里面
    stack = {1: x}
    for index in range(1, len(chain)):
        k = chain[index]
        j = chain[index - 1]
        i = k - j  # here we know this is a chain, therefore i is definitely in the dict
        stack[k] = stack[i] * stack[j]
    return stack[chain[-1]]


## Q8 ##
def power_tree_chain(n):
    tree = PowerTree()
    while n not in tree.parent:
        tree.add_layer()
    return tree.path_from_root(n)


def power_tree_pow(x, n):
    if n == 0:
        return 1
    chain = power_tree_chain(n)
    return power_from_chain(x, chain)


## Q9 ##
def cost_power_tree_pow(n):
    # since in power_from_chain, we multiply once for each loop and we loop it for len(chain) - 1 times
    if n == 0 or n == 1:
        return 0
    chain = power_tree_chain(n)
    return len(chain) - 1


def compare_costs(m):
    num_cost_power = cost_power_tree_pow(m)
    num_cost_bin = cost_bin_pow(m)
    num_cost_factor = cost_factor_pow(m)
    return (num_cost_power, num_cost_bin, num_cost_factor)
