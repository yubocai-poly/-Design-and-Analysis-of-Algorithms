from dg import *


# Question 5
def contains_pattern(s, text):
    s = NFA(s)
    for i in range(len(text)):
        if s.check_text(text[i:]):
            return True
    return False


class NFA:  # 非确定性有限自动机

    def __init__(self, s):  # s is the string containing the regular expression
        self.s = s
        self.m = len(self.s)
        self.dg = DG(len(s) +
                     1)  # the directed graph that stores the epsilon links
        self.lp = [-1 for _ in range(len(s))]
        self.rp = [-1 for _ in range(len(s))]
        self.left_right_match_or(
        )  # assigns lp and rp according to parentheses matches
        self.build_eps_links()  # assigns the epsilon links in self.dg

    def __str__(self):
        n = self.m
        str_lp = 'lp: '
        str_rp = 'rp: '
        for i in range(self.m):
            if self.lp[i] == -1:
                str_lp += '-1  '
            elif self.lp[i] < 10:
                str_lp += str(self.lp[i]) + '   '
            else:
                str_lp += str(self.lp[i]) + '  '
            if self.rp[i] == -1:
                str_rp += '-1  '
            elif self.rp[i] < 10:
                str_rp += str(self.rp[i]) + '   '
            else:
                str_rp += str(self.rp[i]) + '  '
        str_lp += '\n'
        str_rp += '\n'

        str_dg = str(self.dg)

        s = '------------------\nRegular expression\n------------------\n' + 're: ' + '   '.join(
            self.s) + '\n'
        return s + str_lp + str_rp  #+ '------------------\nCorresponding NFA\n------------------\n' + str_dg

    ## Question 1
    def left_right_match(self):
        # we use a list to simulate a stack
        stack = []
        for i in range(self.m):
            if self.s[i] == '(':
                stack.append(i)
            elif self.s[i] == ')':
                j = stack.pop()
                self.lp[i] = j
                self.rp[j] = i

    ## Question 2
    def left_right_match_or(self):
        # now we start to considerate '|' here
        # we first dealing with the left racket
        self.left_right_match()
        stack_left = []
        stack_right = []
        for i in range(self.m):
            if self.s[i] == '(':
                stack_left.append(i)
            elif self.s[i] == '|':
                j = stack_left.pop()
                self.lp[i] = j
        # then we deal with the right racket
        for i in range(self.m - 1, -1, -1):
            if self.s[i] == ')':
                stack_right.append(i)
            elif self.s[i] == '|':
                j = stack_right.pop()
                self.rp[i] = j

    ## Question 3
    def build_eps_links(self):
        for i in range(self.m):
            if (self.s[i] == '|'):
                self.dg.add_link(self.lp[i], i + 1)
                self.dg.add_link(i, self.rp[i])
            if (self.s[i] == '(') or (self.s[i] == ')'):
                self.dg.add_link(i, i + 1)
            if (self.s[i] == '*'):
                self.dg.add_link(i, self.lp[i - 1])
                self.dg.add_link(self.lp[i - 1], i)
                self.dg.add_link(i, i + 1)

    ## Question 4
    # Complexity:
    """
    For all the characters in the text, we need to use eps_links to do the search. In the graph we have m+1 vertices
    and O(m) edges, since for each vertex we have maximum 4 neighbors, so the complexity is O(4m)=O(m). And since the
    length of the text is n, so the complexity is O(mn).
    """

    # Because:
    def check_text(self, w):
        start = [0]
        for S in w:
            now = self.dg.explore_from_subset(start)
            start = []
            for v in now:
                if (v == self.m):
                    return True
                if (self.s[v] == '.') or (self.s[v] == S):
                    start.append(v + 1)
                    if (v + 1 == self.m):
                        return True
            if (len(start) == 0):
                return False

        now = self.dg.explore_from_subset(start)
        for v in now:
            if (v == self.m):
                return True
        return False
