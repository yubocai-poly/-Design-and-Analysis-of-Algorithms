# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
import random


# 布尔可满足性问题 (Boolean Satisfiability Problem, SAT)
class Sat:

    def __init__(self, n, L):
        self.nr_var = n  # variables are x1,...,xn
        self.clauses = L  # list of clauses like [[1,3],[2,-4,-6],[-5,-1,4]]
        self.values = [True for i in range(n + 1)
                       ]  # position 0 in this list is not used
        self.fixed = {}  # 字典存储已经固定的clause变量

    # Question 1

    def is_clause_satisfied(self, c):
        # 检测一个clause是否满足self.values
        for var in c:
            if var > 0 and self.values[var]:
                return True
            if var < 0 and not self.values[-var]:  # 注意这里是not并且是var是负数
                return True

        return False

    def satisfied(self):
        for clause in self.clauses:
            if not self.is_clause_satisfied(clause):
                return False

        return True

    # Questions 2 & 8

    def initialize(self):
        # TO COMPLETE
        # 随机设置self.values的值
        for i in range(1, self.nr_var + 1):
            if not i in self.fixed: # 第八题的优化
                self.values[i] = random.choice([True, False])


    def walk_sat(self, N):
        # TO COMPLETE
        if N == 0:
            return
        self.clauses.sort(key=len)
        satisfy = False
        for i in range(0, 2**len(self.values)):
            if i % N == 0:
                self.initialize()
            satisfy = True
            for clause in self.clauses:
                if not self.is_clause_satisfied(clause):
                    satisfy = False
                    change_index = random.randint(0, len(clause) - 1)
                    var_index = abs(clause[change_index])
                    if self.values[var_index]:
                        self.values[var_index] = False
                    else:
                        self.values[var_index] = True
                    break
            if satisfy:
                break
        return satisfy

    ##################################################
    # Propagation of fixed variables in a CNF formula
    ##################################################

    # Question 6

    def fix_values_from_1clauses(self):
        # TO COMPLETE
        found1clause = False
        for el in self.clauses:
            if len(el) == 1:
                found1clause = True
                value = el[0]
                if value > 0:
                    self.values[value] = True
                    self.fixed[value] = True
                else:
                    self.values[-value] = False
                    self.fixed[-value] = False

        return found1clause

    # Helper functions for Question 7

    def simplify_clause(self, c):
        res = []
        for x in c:
            if not abs(x) in self.fixed:
                res.append(x)
            else:
                if (x > 0 and self.values[x]) or (x < 0
                                                  and not self.values[-x]):
                    return -1
        return res

    def simplify_clauses(self):
        res = []
        for c in self.clauses:
            cp = self.simplify_clause(c)
            if not cp == -1:
                res.append(cp)
        return res

    # Question 7

    def simplify_formula_by_propagation(self):
        # TO COMPLETE
        finish = False
        while not finish:
            finish = True
            if self.fix_values_from_1clauses():  # 如果能够继续知道1-clause，则接着优化
                finish = False
            self.clauses = self.simplify_clauses()  # 根据字典的固定值优化clause

    ##################################################
    # DISPLAY METHODS
    ##################################################

    def clause_to_string(self, c):
        res = ""
        for i in range(0, len(c)):
            if i == 0: res = "("
            else: res = res + " ∨ "
            if (c[i] > 0): res = res + "x" + str(c[i])
            else: res = res + "¬x" + str(-c[i])
        return res + ")"

    def display_statistics(self):
        print("Number of clauses: " + str(len(self.clauses)))
        print("Number of non-fixed variables: " +
              str(self.nr_var - len(self.fixed)))
        print("")

    def display_formula(self):
        L = self.clauses
        res = self.clause_to_string(L[0])
        for i in range(1, len(L)):
            res = res + " ∧ " + self.clause_to_string(L[i])
        print(res)

    def display_values(self):
        res = ""
        for i in range(1, self.nr_var + 1):
            res = res + "x" + str(i) + "=" + str(self.values[i]) + " "
        print(res)
