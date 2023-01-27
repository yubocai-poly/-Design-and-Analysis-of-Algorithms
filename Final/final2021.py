class Node:
  def __init__(self, key ,left=None, right=None, size = 0):
    self.key = key
    self.left = left
    self.right = right
    self.size = size
    
class BST:
  def __init__(self):
    self.root = None
    
  def insert(self, key):
    self.root = self._insert(self.root, key)
    
  def _insert(self, node, key):
    if node is None:
      return Node(key)
    if key < node.key:
      node.left = self._insert(node.left, key)
    else:
      node.right = self._insert(node.right, key)
    node.size = 1 + self.size(node.left) + self.size(node.right)
    return node
  
  def select(self, k):
    return self._select(self.root, k)
  
  def _select(self, node, k):
    if node is None:
      return None
    t = self.size(node.left)
    if t > k:
      return self._select(node.left, k)
    elif t < k:
      return self._select(node.right, k-t-1)
    else:
      return node.key
    
    
# Test Cases
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Test select method
print(bst.select(0)) # should return 2
print(bst.select(3)) # should return 5
print(bst.select(5)) # should return 7
