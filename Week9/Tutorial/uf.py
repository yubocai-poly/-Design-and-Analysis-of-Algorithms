# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Yubo Cai


# An efficient union–find implementation
class UF_base:
    '''
        basic Union-Find implementation, implementing Quick-find
    '''

    def __init__(self, N):
        self.N = N  # number of elements
        self.A = [i for i in range(N)]  # the array representing the forest
        self.count = N  # number of connected components

        # p: 0 1 2 3 4 5 6 7 8 9 10 11
        # A[p]: 0 1 2 0 1 2 3 1 2 6 4 2

    def get_N(self):
        return self.N

    def get_count(self):
        return self.count

    def union(self, p, q):
        if self.is_connected(p, q):
            return

        # merging the classes of p and q
        self.count -= 1
        r1 = self.find(p)
        r2 = self.find(q)

        # all the elements with root r2 now has root r1
        for i in range(self.N):
            if self.A[i] == r2:
                self.A[i] = r1

    def find(self, p):
        # A function find(p) that finds the element representing the equivalence class of p, i.e. finding
        # the root of the tree where p belongs.
        return self.A[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Rank_UF(UF_base):

    def __init__(self, N):
        super().__init__(N)
        self.ranks = [1 for _ in range(N)]

    # Question 1
    def union(self, p, q):
        '''
        TO IMPLEMENT
        '''
        rank1 = self.find(p)
        rank2 = self.find(q)

        if rank1 == rank2:
            return

        self.count -= 1

        if self.ranks[rank1] > self.ranks[rank2]:
            self.A[rank2] = rank1
        else:
            self.A[rank1] = rank2

        if self.ranks[rank1] == self.ranks[rank2]:
            self.ranks[rank1] += 1

    # Question 2
    def find(self, p):
        '''
        TO IMPLEMENT
        '''
        if self.A[p] == p:
            return p
        else:
            return self.find(self.A[p])
