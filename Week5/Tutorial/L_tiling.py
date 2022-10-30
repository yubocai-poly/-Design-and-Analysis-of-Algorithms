# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-10-20


# Tiling by L-shapes
# Question 1
def middleL(n, i, j, a, b):
    # returns the middle of the punctured grid of type (n, i, j, a, b)
    if n == 0:
        return [(i, j)]

    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)
    res = []

    if a < i2:
        res = [(i2, j2), (i2, j2 - 1)]
        if b < j2:
            res.append((i2 - 1, j2))
        else:
            res.append((i2 - 1, j2 - 1))
    else:
        res = [(i2 - 1, j2 - 1), (i2 - 1, j2)]
        if b < j2:
            res.append((i2, j2))
        else:
            res.append((i2, j2 - 1))
    return res


# Question 2
def lower_left_hole(n, i, j, a, b):
    # returns the coordinates of the hole of the lower left quadrant
    if n == 0:
        return [(i, j)]

    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)

    if a < i2 and b < j2:
        return a, b
    else:
        return i2 - 1, j2 - 1


def lower_right_hole(n, i, j, a, b):
    # returns the coordinates of the hole of the lower right quadrant
    if n == 0:
        return [(i, j)]

    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)

    if a >= i2 and b < j2:
        return a, b
    else:
        return i2, j2 - 1


def upper_left_hole(n, i, j, a, b):
    # returns the coordinates of the hole of the upper left quadrant
    if n == 0:
        return [(i, j)]

    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)

    if a < i2 and b >= j2:
        return a, b
    else:
        return i2 - 1, j2


def upper_right_hole(n, i, j, a, b):
    # returns the coordinates of the hole of the upper right quadrant
    if n == 0:
        return [(i, j)]

    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)

    if a >= i2 and b >= j2:
        return a, b
    else:
        return i2, j2


# Question 3
def tile(n, i, j, a, b):
    # returns a list with a valid L-tiling of the punctured grid of type (n, i, j, a, b)
    tiling_list = []
    if n == 0:
        return tiling_list
    tiling_list.append(middleL(n, i, j, a, b))
    i2 = i + 2**(n - 1)
    j2 = j + 2**(n - 1)
    k, l = lower_left_hole(n, i, j, a, b)
    tiling_list += tile(n - 1, i, j, k, l)
    k, l = lower_right_hole(n, i, j, a, b)
    tiling_list += tile(n - 1, i2, j, k, l)
    k, l = upper_left_hole(n, i, j, a, b)
    tiling_list += tile(n - 1, i, j2, k, l)
    k, l = upper_right_hole(n, i, j, a, b)
    tiling_list += tile(n - 1, i2, j2, k, l)
    
    return tiling_list
