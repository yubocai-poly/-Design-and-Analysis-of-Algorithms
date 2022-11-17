#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import math

#Q5
def compute_witness_trivial(A,B):
    n = len(A)
    W = []
    for i in range(n):
        W.append([0]*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i][k]*B[k][j] == 1:
                        W[i][j] = k+1
    return W
                
            
    
#Complexity: O(n^3)


#Q6
def expose_column(A):
    pass
    
#Q6
def compute_witness_unique(A,B):
    pass
#Complexity: O(n^2)

#Q7
def nullify_columns(A,R):
    pass
    
#Q7
def nullify_rows(A,R):
    pass

#Q7
def compute_witness_restricted(A,B,R):
    pass
#Complexity: O(n^2)0

#Q8
#(1/2e)^(2*e*log(n))

#Q9
def sample(r,n):
    pass

#Q10
def compute_witness_random(A,B):
   pass
                
        
                   

# =============================================================================
# Matrix operations
# =============================================================================

def inverse(A):  
    C = [[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = -A[i][j]
    return C

def multiply_matrices(A,B):
    X = np.array(A)
    Y = np.array(B)
    Z = np.matmul(X,Y)
    return Z.tolist()










