#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


#Q6
def mult_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


#Q7
def cost_mult_matrix(n):
    res=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res += 2
    return res

#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    A=np.array(A)
    row, col = A.shape
    row2, col2 = row//2, col//2
    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[row2:, :col2].tolist(), A[row2:, col2:].tolist()

def merge(a,b,c,d):
    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()

def add_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C

def sub_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
    return C

#Q8
def strassen(A,B):
    n = len(A)
    if n == 1:
        temp = A[0][0]*B[0][0]
        return [[temp]]
 
    a, b, c, d = split(A)
    x, y, z, t = split(B)
 
    q1 = strassen(a, add_matrix(x,z)) 
    q2 = strassen(d, add_matrix(y,t))       
    q3 = strassen(sub_matrix(d,a), sub_matrix(z,y))       
    q4 = strassen(sub_matrix(b,d), add_matrix(z,t))       
    q5 = strassen(sub_matrix(b,a), z)       
    q6 = strassen(sub_matrix(c,a), add_matrix(x,y)) 
    q7 = strassen(sub_matrix(c,d), y) 
 
    c11 = add_matrix(q1,q5) 
    c12 = add_matrix(add_matrix(q2,q3),sub_matrix(q4,q5))          
    c21 = add_matrix(add_matrix(q1,q3),sub_matrix(q6,q7))          
    c22 = add_matrix(q2,q7)
 
    c = merge(c11,c12,c21,c22)

    return c

#Q9
def cost_strassen(n):
    if n==0: return 1
    tmp=cost_strassen(n-1)
    return (7*tmp+18*(2**(n-1))**2)


#Q10
def convert_01(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if ((A[i][j]>0)): A[i][j]=1
            else: A[i][j]=0
    return A

#Q11
def matrix_bool_add(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] or B[i][j]
    return C

def matrix_power(A,n):
    if n==1: return A
    tmp=matrix_power(A,n//2)
    tmp=strassen(tmp,tmp)
    if n%2==0: return tmp
    return strassen(tmp,A)


def transitive_closure(A):
    n = len(A)
    # C is initialized as the identity matrix I_n
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        C[i][i]=1
    if n==1: return C  
    C=matrix_bool_add(C,A)
    if n==2: return C  
    # tmp contains the current power of A
    tmp = matrix_power(C,n-1)
    return convert_01(tmp)







