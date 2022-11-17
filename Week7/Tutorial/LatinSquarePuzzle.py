# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
from Sat import *


class LatinSquarePuzzle:

    def __init__(self, k, initial):
        self.k = k
        self.initial = initial
        self.sat = Sat(self.k**3, [])  # n = k^3, L = []
        self.final = []

    def triple_to_int(self, v, i, j):
        return (i * self.k + j) * self.k + v + 1

    def int_to_triple(self, r):
        temp = r - 1
        v = temp % self.k

        temp //= self.k
        j = temp % self.k

        temp //= self.k
        i = temp % self.k

        return [v, i, j]

    # Question 3

    def build_generic_clauses(self):
        # TO COMPLETE
        for i in range(self.k):
            for j in range(self.k):
                # 实现三个步骤的算法
                self.sat.clauses.append([
                    self.triple_to_int(v, i, j) for v in range(self.k)
                ])  # v, i, j for v变化
                self.sat.clauses.append([
                    self.triple_to_int(i, j, v) for v in range(self.k)
                ])  # v, i, j for j变化
                self.sat.clauses.append([
                    self.triple_to_int(j, v, i) for v in range(self.k)
                ])  # v, i, j for i变化
                # 下面计算clause -x_v1ij \/ -x_v2ij for 0 < v1 < v2 < k
                for v1 in range(1, self.k):
                    for v2 in range(v1):
                        self.sat.clauses.append([
                            -self.triple_to_int(v1, i, j),
                            -self.triple_to_int(v2, i, j)
                        ])
                        self.sat.clauses.append([
                            -self.triple_to_int(j, v1, i),
                            -self.triple_to_int(j, v2, i)
                        ])
                        self.sat.clauses.append([
                            -self.triple_to_int(i, j, v1),
                            -self.triple_to_int(i, j, v2)
                        ])

    # Question 4

    def add_fixed_value_clauses(self):
        # TO COMPLETE
        for i in range(self.k):
            for j in range(self.k):
                if self.initial[i][j] != '*':
                    self.sat.clauses.append(
                        [self.triple_to_int(self.initial[i][j], i, j)])

    # Questions 5 & 8

    def solve(self):
        # TO COMPLETE
        self.build_generic_clauses()
        self.add_fixed_value_clauses()
        #第八题的优化
        self.sat.simplify_formula_by_propagation()
        f = self.sat.nr_var - len(self.sat.fixed)
        if f > 0:
            N = 4 * f**2
            self.sat.walk_sat(N)
        # 初始化final
        result = []
        for i in range(self.k):
            result.append(['x'] * self.k)
        print(len(self.sat.values))
        print(self.sat.values)
        for i in range(1, self.sat.nr_var + 1):
            if self.sat.values[i]:
                [v, i, j] = self.int_to_triple(i)
                if result[i][j] == 'x':
                    result[i][j] = v

        self.final = result

    ##################################################
    # DISPLAY METHODS
    ##################################################

    def display_before_solving(self, prefix=""):
        print(prefix + "Initial configuration:")
        for r in range(self.k):
            print(prefix +
                  "[{0}]".format(', '.join(map(str, self.initial[r]))))
        print("")

    def display_after_solving(self, prefix=""):
        if (len(self.final) == 0):
            print(prefix + "Not yet solved")
            return
        print(prefix + "Solved configuration:")
        for r in range(self.k):
            print(prefix + "[{0}]".format(', '.join(map(str, self.final[r]))))
        print("")
