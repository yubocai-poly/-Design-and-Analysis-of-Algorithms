# -*- coding: utf-8 -*-


def str_compare(a, b):
    N = min(len(a), len(b))
    for i in range(N):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1

    return len(a) - len(b)


def str_compare_m(a, b, m):
    if len(a) >= m and len(b) >= m:
        # len(a) >= m and len(b) >= m
        return str_compare(a[:m], b[:m])
    else:
        # len(a) < m or len(b) > m
        return str_compare(a, b)


def longest_common_prefix(a, b):
    N = min(len(a), len(b))
    for i in range(N):
        if a[i] != b[i]:
            return i
    return N


class suffix_array:
    # Question 1
    def __init__(self, t):
        self.T = t
        self.N = len(t)
        self.suffId = [i for i in range(self.N)]
        self.suffId.sort(key=lambda i: self.T[i:])
        """
        1. For the time complexity, we have C(n) = C(n/2) + O(N^2) by the master theorem we have the time complexity is O(N^2 log N)
        2. For the space, we have S(n) = S(n / 2) + O(N) this is because every time we compare two string, we need O(N) space to store the string, 
        by the master theorem, we have the spcae is O(N log N)
        """

        # TODO: order suffId by lexicographic order
        # SORT

    def suffix(self, i):
        return self.T[self.suffId[i]:]

    # Question 2
    def findL(self, S):
        # TO IMPLEMENT
        m = len(S)
        l = -1
        r = self.N

        while l + 1 < r:
            mid = (l + r) // 2
            if str_compare_m(self.suffix(mid), S, m) < 0:
                l = mid
            else:
                r = mid

        return r

    # Question 2
    def findR(self, S):
        # TO IMPLEMENT
        m = len(S)
        r = self.N
        l = -1

        while l + 1 < r:
            mid = (l + r) // 2
            if str_compare_m(self.suffix(mid), S, m) <= 0:
                l = mid
            else:
                r = mid

        return r

    # Question 3 (optional)
    def findLR(self, S):
        return (self.findL(S), self.findR(S))


# Question 4
def KWIC(sa, S, c=15):
    # TO IMPLEMENT
    m = len(S)
    l = sa.findL(S)
    r = sa.findR(S)
    result = []
    for i in range(l, r):
        result.append(sa.T[max(0, sa.suffId[i] - c):sa.suffId[i] + m + c])
    return result


# Question 5
def longest_repeated_substring(sa):
    # TO IMPLEMENT
    result = ''
    max_len = 0
    for i in range(1, sa.N):
        lcp = longest_common_prefix(sa.suffix(i), sa.suffix(i - 1))
        if lcp > max_len:
            max_len = lcp
            result = sa.suffix(i)[:lcp]

    return result
