# -*- coding: utf-8 -*-

import math
from PowerTree_sol import *

# binary powering, returns x^n
def bin_pow(x,n):
 if n==0: return 1
 tmp=bin_pow(x,n//2)
 tmp=tmp*tmp
 if n%2==0: return tmp
 return tmp*x

# returns the number of multiplications of a call to
# bin_pow(x,n)
def cost_bin_pow(n):
 if n<=1: return 0
 if n%2==0:
   return 1+cost_bin_pow(n//2)
 else:
   return 2+cost_bin_pow(n//2)

# returns -1 if n is prime, and returns the smallest factor
# p>=2 of n if n is composite
def smallest_factor(n):
 j=int(math.sqrt(n))
 for i in range(2,j+1):
   if n%i==0: return i
 return -1

# factorization powering, returns x^n
def factor_pow(x,n):
 if n==0: return 1
 if n==1: return x
 p=smallest_factor(n)
 if p>=0:
   y=factor_pow(x,p)
   q=n//p
   return factor_pow(y,q)
 else:
   return x*factor_pow(x,n-1)

# returns the number of multiplications of a call to
# factor_pow(x,n)
def cost_factor_pow(n):
 if n<=1: return 0
 p=smallest_factor(n)
 if p>=0: return cost_factor_pow(p)+cost_factor_pow(n//p)
 else: return 1+cost_factor_pow(n-1)

# returns x^n from an addition chain of n (stored in the parameter chain)
def power_from_chain(x,chain):
  powers={1:x}
  for s in range(1,len(chain)):
    k=chain[s]
    j=chain[s-1]
    i=k-j
    powers[k]=powers[i]*powers[j]
  return powers[chain[-1]]

# returns the addition chain for n (path from the root
# to n in the power tree) after inserting enough
# layers of the tree so that n is part of it
def power_tree_chain(n):
  tree=PowerTree()
  while n not in tree.parent:
    tree.add_layer()
  return tree.path_from_root(n)

# power tree powering, returns x^n
def power_tree_pow(x,n):
  if n==0: return 1
  chain= power_tree_chain(n)
  return  power_from_chain(x,chain)

# number of multiplications of a call to power_tree_pow(x,n)
# does not count the cost of building the tree
def cost_power_tree_pow(n):
  if n==0: return 0
  chain= power_tree_chain(n)
  return len(chain)-1

# prints the compared costs
def compare_costs(m):
    print("bin_pow | factor_pow | power_tree_pow")
    for n in range(m+1):
        print("n="+str(n)+": "+str(cost_bin_pow(n))+' | '+str(cost_factor_pow(n))+' | '+str(cost_power_tree_pow(n)))
