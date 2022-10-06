#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-9-29

import numpy as np


#Q6
def mult_matrix(A, B):
    # Here A and B are sqaure matrices of the same size
    n = len(A)
    # we create a zero matrix of the same size as A and B
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


#Q7
def cost_mult_matrix(n):
    # 这里我们每次需要一个加和一个乘操作，因此总的操作次数为 2n^3
    return (1 + 1) * n**3


#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    A = np.array(A)
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[
        row2:, :col2].tolist(), A[row2:, col2:].tolist()


def merge(a, b, c, d):
    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()


#Computes the matrix A+B
def add_matrix(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


#Computes the matrix A-B
def sub_matrix(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


#Q8
def strassen(A, B):
    n = len(A)
    if n == 1:
        return mult_matrix(A, B)
    a, b, c, d = split(A)[0], split(A)[1], split(A)[2], split(A)[3]
    x, y, z, t = split(B)[0], split(B)[1], split(B)[2], split(B)[3]
    q1 = strassen(a, add_matrix(x, z))
    q2 = strassen(d, add_matrix(y, t))
    q3 = strassen(sub_matrix(d, a), sub_matrix(z, y))
    q4 = strassen(sub_matrix(b, d), add_matrix(z, t))
    q5 = strassen(sub_matrix(b, a), z)
    q6 = strassen(sub_matrix(c, a), add_matrix(x, y))
    q7 = strassen(sub_matrix(c, d), y)
    return merge(add_matrix(q1, q5),
                 add_matrix(add_matrix(q2, q3), sub_matrix(q4, q5)),
                 add_matrix(add_matrix(q1, q3), sub_matrix(q6, q7)),
                 add_matrix(q2, q7))


#Q9
def cost_strassen(n):
    # Here A and B are sqaure matrices of the size 2^n
    if n == 0:
        return 1
    recur = cost_strassen(n - 1)
    return 7 * recur + 18 * (2**(n - 1))**2
    # 7 个递归调用，每个递归调用的复杂度为 recur
    # 然后分割出来的每个矩阵的大小为 2^(n-1)，每个矩阵需要 18 次操作 每次操作是相加所以是把 2^(n-1) 平方中间所有的数全部相加一次


# Transitive closure of a graph
#Q10
def convert_01(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] > 0:
                A[i][j] = 1
    return A


#Q11
def add_bool_matrix(A, B):
    # 这里我们相加两个bool矩阵，因此我们需要把矩阵中的非零元素全部变成1
    n = len(A)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1 or B[i][j] == 1:
                result[i][j] = 1
    return result


def matrix_power(A, n):
    if n == 1:
        return A
    tmp = matrix_power(A, n // 2)
    tmp = strassen(tmp, tmp)
    if n % 2 == 0:
        return tmp
    return strassen(tmp, A)


def transitive_closure(A):
    n = len(A)
    if n == 1:
        return A
    Id = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        Id[i][i] = 1
    result = add_bool_matrix(Id, A)
    tmp = matrix_power(result, n - 1)
    return convert_01(tmp)
