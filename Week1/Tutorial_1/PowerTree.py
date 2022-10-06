# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-9-22


## Q7 ##
class PowerTree:

    def __init__(self):
        self.layers = [[1]]
        self.parent = {1: 1} # {1: 1, 2: 1, 3: 2, 4: 2} key是节点，value是父节点

    def draw_tree(self):
        for i in range(len(self.layers)):
            print("layer", i)
            for j in self.layers[i]:
                print(j, "->", self.parent[j])

    def path_from_root(self, k):
        # 这个函数的功能是返回从根节点到k的路径，如果k不在树中，返回-1
        if k not in self.parent:
            return -1
        res = [k]
        while (k != 1): # 这里我们一直往上找，直到找到根节点
            k = self.parent[k]
            res = [k] + res
        return res

    def add_layer(self):
        # 这个函数的功能是添加一层，我调用一次加一层，然后加的一层的数据添加到layers和parent中
        layer_now = self.layers[-1]
        layer_next = []
        for el in layer_now:
            # 这里我们去看前面路径和是不是在parent中，如果不在，就添加到parent中
            for path_node in self.path_from_root(k=el):
                k = el + path_node
                if k not in self.parent:
                    layer_next.append(k)  # 这里添加到layer_next中，找到了新的一层的节点
                    self.parent[k] = el  # 这里添加到parent中

        # 最后我们将新的一层添加到layers中
        self.layers.append(layer_next)


## Program Test ##
def test7():
    tree = PowerTree()
    # We add 4 layers here
    for i in range(7):
        tree.add_layer()
    print(tree.layers)
    print(tree.path_from_root(k=10))  # expected: [1, 2, 5, 10]


test7()