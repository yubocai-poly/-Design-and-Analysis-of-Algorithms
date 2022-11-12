# -*- coding: utf-8 -*-

# Q1

def poly_mult(P,Q):
    n=len(P)
    m=len(Q)
    R=[0 for i in range(m+n-1)]
    for i in range(n):
        for j in range(m):
            R[i+j]=R[i+j]+P[i]*Q[j]
    return R   

def cost_poly_mult(n): 
    return 2*n**2-2*n+1     

# Q2

def poly_add(P,Q): 
   n=len(P)
   m=len(Q)
   R=[0 for i in range(max(m,n))]
   for i in range(n):
       R[i]+=P[i]
   for i in range(m):
       R[i]+=Q[i]
   return R    
         
def neg(P):
   return [-P[i] for i in range(len(P))]
   
def shift(P,k):
   return [0 for i in range(k)]+[P[i] for i in range(len(P))]
  
# Q3  
  
def poly_kara_mult(P,Q):
    assert len(P) == len(Q), "this method only works when P and Q have the same number of coefficients"
    n=len(P)
    if n==1:
        return [P[0]*Q[0]]
    n2=n//2
    P0=[P[i] for i in range(n2)]
    P1=[P[i] for i in range(n2,n)]
    Q0=[Q[i] for i in range(n2)]
    Q1=[Q[i] for i in range(n2,n)] 
    A=poly_kara_mult(P0,Q0)
    B=poly_kara_mult(P1,Q1)    
    C=poly_kara_mult(poly_add(P0,P1),poly_add(Q0,Q1))
    D=poly_add(poly_add(C,neg(A)),neg(B))
    return poly_add(poly_add(A,shift(D,n2)),shift(B,2*n2))
    
def cost_poly_kara_mult(n):
    if n==1: 
        return 1
    else:
        return 4*n+3*cost_poly_kara_mult((n+1)//2)

#print([cost_poly_kara_mult(n) for n in range(1,15)])        

# Q4 

def cost_poly_tc3_mult(n):#donner formule
    if n==1: 
        return 1
    elif n==2: 
        return 3
    else:
        return 30*n+5*cost_poly_tc3_mult((n+2)//3)
        
print("tc3: {}".format([cost_poly_tc3_mult(n) for n in range(1,15)]))
    
# Q5 hybride
   
def poly_switch_mult(d,P,Q):
    assert len(P) == len(Q), "this method only works when P and Q have the same number of coefficients"
    n=len(P)
    if n<=d:
        return poly_mult(P,Q)
    n2=n//2
    P0=[P[i] for i in range(n2)]
    P1=[P[i] for i in range(n2,n)]
    Q0=[Q[i] for i in range(n2)]
    Q1=[Q[i] for i in range(n2,n)] 
    A=poly_switch_mult(d,P0,Q0)
    B=poly_switch_mult(d,P1,Q1)    
    C=poly_switch_mult(d,poly_add(P0,P1),poly_add(Q0,Q1))
    D=poly_add(poly_add(C,neg(A)),neg(B))
    return poly_add(poly_add(A,shift(D,n2)),shift(B,2*n2))

def cost_switch_mult(d,n):
    if n<=d:
        return 2*n**2-2*n+1
    else:
        n2=(n+1)//2
        return 4*n+3*cost_switch_mult(d,n2)

