# -*- coding: utf-8 -*-

### Question 1 ###
def peak_naive(L):
    # TO IMPLEMENT
    if len(L) == 1:
        return 0
    for i , e in enumerate(L):
        if i == 0:
            if e >= L[i+1]:
                return i
        elif i == len(L)-1:
            if e >= L[i-1]:
                return i
        else:
            if e >= L[i-1] and e >= L[i+1]:
                return i
        
    
### Question 2 ###   
def peak(L):    
    # TO IMPLEMENT
    return peak_aux(L,0,len(L))
    
def peak_aux(L,p,q):    
    # TO IMPLEMENT
    if q - p < 2:
        return p
    l = (p+q)//2  
    if L[l] < L[l-1]:
        return peak_aux(L,p,l)
    elif L[l-1] < L[l]:
        return peak_aux(L,l,q)
    else:
        return l

    
### Question 3 ###
def is_peak(M,i,j):
    # TO IMPLEMENT
    is_p = True
    if not i - 1 < 0:
        is_p = is_p and M[i][j] >= M[i-1][j]
    if not i + 1 >= len(M):
        is_p = is_p and M[i][j] >= M[i+1][j]
    if not j - 1 < 0:
        is_p = is_p and M[i][j] >= M[i][j-1]
    if not j + 1 >= len(M[0]):
        is_p = is_p and M[i][j] >= M[i][j+1]
    return is_p

    
### Question 4 ###
def peak2d_naive(M):
    # TO IMPLEMENT
    for i in range(len(M)):
        for j in range(len(M[0])):
            if is_peak(M,i,j):
                return (i,j)

### Question 5 ###
def pivot(M,p,q,r,s):    
    # TO IMPLEMENT
    l = (p+q)//2
    m = (r+s)//2
    if q - p ==1 :
        PQ = [p]
    else:
        PQ = [p, l-1, l, q-1]
    if s - r ==1 :
        RS = [r]
    else:
        RS = [r, m-1, m, s-1]

    maxi = a = b = 0
    
    
    for i in PQ:
        for j in range(r,s):
            if M[i][j] > maxi:
                maxi = M[i][j]
                a = i
                b = j
    for j in RS:
        for i in range(p,q):
            if M[i][j] > maxi:
                maxi = M[i][j]
                a = i
                b = j
    return (a,b)

    
### Question 6 ###
def peak2d(M):    
    # TO IMPLEMENT
    return peak2d_aux(M,0,len(M),0,len(M[0]))
  
def peak2d_aux(M,p,q,r,s):
    # TO IMPLEMENT
    if q - p <= 4 or s - r <= 4:
        return pivot(M,p,q,r,s)
    l = (p+q)//2
    m = (r+s)//2
    a,b = pivot(M,p,q,r,s)
    if a < l:
        q = l
    elif a > l:
        p = l+1
    if b < m:
        s = m
    elif b > m:
        r = m+1
    return peak2d_aux(M,p,q,r,s)

    

