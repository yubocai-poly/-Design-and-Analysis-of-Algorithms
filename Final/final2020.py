# CSE202 - Design and Analysis of Algorithms
# Final Exam 2020


class Node:

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def rotateright(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        return tmp

    def rotateleft(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        return tmp

    def insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self.insert(node.left, key, value)
            if node.value < node.left.value:
                node = self.rotateright(node)

        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            if node.value < node.right.value:
                node = self.rotateleft(node)

        return node
