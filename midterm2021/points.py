#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import numpy as np
import random
import math


#Q1
def min_max_aux(A, left, right):
    if left == right - 1:
        return A[left], A[left]
    n = (left + right) // 2
    min1, max1 = min_max_aux(A, left, n)
    min2, max2 = min_max_aux(A, n, right)
    return (min(min1, min2), max(max1, max2))


def min_max(A):
    # This function returns both the minimum and the maximum of A
    return min_max_aux(A, 0, len(A))


#Recurrence relation: T(n) = 2T(n/2) + 2
#Values for the first terms:
#    n = 1: T(n) = 0
#    n = 2: T(n) = 2*0+2 = 2


#Q2
# This function returns the coordinates of both the top-left and bottom-right corners.
def bounding_box(S):
    if len(S) == 1:
        return S
    x = []
    y = []
    for el in S:
        x.append(el[0])
        y.append(el[1])
    x_min, x_max = min_max(x)
    y_min, y_max = min_max(y)
    return [[x_min, y_max], [x_max, y_min]]


#Q3
# Compute the maxima set
def maxima_set(S):
    n = len(S)
    if n <= 1:
        return S
    k = n // 2
    S1 = maxima_set(S[:k])
    S2 = maxima_set(S[k:])
    q = S2[0]
    for element in S1:
        if element[0] <= q[0] and element[1] <= q[1]:
            S1.remove(element)

    return S1 + S2


#Recurrence relation: T(n) = 2T(n/2) + 2*(n/2) = 2T(n/2) + n

#Q4
def dominated(C, left, right, b):
    if left == right - 1:
        if b >= C[0][1]:
            return 1
        else:
            return 0
    k = (left+right)//2
    if b >= C[k][1]:
        return k + dominated(C, k, right, b)
    else:
        return dominated(C, left, k, b)
    
def my_y_coordinate(A):
    return A[1]

def dominance_counting(S):
    n = len(S)
    if n == 0:
        return []
    if n == 1:
        return [[S[0], 0]]
    
    k = n//2
    S1 = dominance_counting(S[:k])
    S2 = dominance_counting(S[k:])
    
    C = S[:k]
    C.sort(key=my_y_coordinate)
    R = []
    for q in S2:
        x, c = q
        a, b = x
        R += [ [x, c + dominated(C, 0, len(C), b)] ]
    return S1 + R

# Auxilliary functions


def lexicographic(p1,p2):
    if (p1[0] < p2[0]):
        return True
    elif (p1[0] == p2[0] ):
        return p1[1] <= p2[1]
    return False

def y_coordinate(A):
    return A[0][1]
    
def sort_y(C):
    C.sort(key=y_coordinate)



S2 = [[2, 6], [3, 7], [4, 5], [6, 4], [8, 6], [9, 3], [10, 2], [11, 2]]
print(dominance_counting(S2))
