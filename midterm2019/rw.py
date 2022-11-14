# -*- coding: utf-8 -*-
# CSE202 - Design and Algorithms Analysis
# Midterm 2019
# Author: Yubo Cai

import random


class Graph:

    def __init__(self, L):
        # vertices are labeled from 0 to n-1
        # L[i] gives the list of neighbours of vertex i
        self.L = L
        self.n = len(L)

    # Question 1
    # draws a random neighbour of vertex i
    def random_neighbour(self, i):
        j = random.randint(0, len(self.L[i]) - 1)
        return self.L[i][j]

    # Question 2
    # draws a random walk of length k, starting from 0
    def random_walk(self, k):
        res = [0]
        m = 0
        for i in range(1, k + 1):
            m = self.random_neighbour(m)
            res.append(m)
        return res

    # Question 3
    # draws a random walk (starting from 0) till all vertices are visited
    def random_walk_till_covered(self):
        res = [0]
        m = 0
        check = {0: 1}
        while (True):
            m = self.random_neighbour(m)
            res.append(m)
            if m in check:
                check[m] += 1
            else:
                check[m] = 1
            if len(check) == self.n:
                return res

    # Question 4
    # draws a random spanning tree
    def random_tree(self):
        parent = {}
        m = 0
        while True:
            j = self.random_neighbour(m)
            if (j != 0) and (j not in parent):
                parent[j] = m
            if len(parent) == self.n - 1:
                return parent
            m = j
