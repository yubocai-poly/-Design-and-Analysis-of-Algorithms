# -*- coding: utf-8 -*-

class PowerTree:
    
  # constructor, initializes the tree with a single node (the root 1)
  # and a single layer (layer 0, containing the root node)  
  def __init__(self): 
    self.layers=[[1]]
    self.parent={1:1}
  	
  # if k is not in the tree (not enough layers built) return -1
  # if k is in the tree, returns a list giving the successive labels
  # on the path from the root (equal to 1) to k
  def path_from_root(self,k):
    if k not in self.parent: return -1
    res=[k]
    while(k!=1):
        k=self.parent[k]	
        res=[k]+res
    return res
    
  # adds the (k+1)th layer to the tree, when the layers
  # already in the tree are 0..k  
  def add_layer(self):
    tab1 = self.layers[-1]
    tab2=[]	
    for j in tab1:
       for h in self.path_from_root(j):
           k=j+h
           if k not in self.parent:
               tab2.append(k)
               self.parent[k]=j
    self.layers.append(tab2)
  
  # displays the layers of the tree
  def draw_tree(self):
    for i in range(len(self.layers)):	
        print("layer",i)
        for j in self.layers[i]: print(j,"->",self.parent[j])
