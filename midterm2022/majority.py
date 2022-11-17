from math import log, log2
from random import randint


## Question 1
# Return frequency of v in L[start:stop].
# The worst-case run time is:
# Because:
def getFrequency(v, L, start, stop):
    L_sub = L[start:stop]
    n = 0
    for el in L_sub:
        if el == v:
            n += 1
    return n


# Question 1 Answer
# The worst-case run time which we list all the element from L[start:stop], which we have O(stop-start)


## Question 2
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is:
# Because:
def getMajorityNaively(L):
    for v in L:
        if getFrequency(v, L, 0, len(L)) > len(L) // 2:
            return v
    return False


# Question 2 Answer
# The worst case which is we have to review all the element until the end of L and check whether this element is the majority element or not
# which gave us the complexity of O(n^2) where n is the length of L


## Question 3
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is:
# Because:
def getMajorityDaC(L):

    def helpGetMajorityDaC(start, stop):
        if stop - start == 1:
            return L[start]
        # Divide and conquer part
        mid = (start + stop) // 2
        left_Majority = helpGetMajorityDaC(start, mid)
        right_Majority = helpGetMajorityDaC(mid, stop)
        if left_Majority == right_Majority:
            return left_Majority
        left_MajorityFreq = getFrequency(left_Majority, L, start, stop)
        right_MajorityFreq = getFrequency(right_Majority, L, start, stop)
        if left_MajorityFreq > (stop - start) // 2:
            return left_Majority
        if right_MajorityFreq > (stop - start) // 2:
            return right_Majority
        return False

    return helpGetMajorityDaC(0, len(L))


# Question 3 Answer
# For the recursive complexity which is C(n) <= 2C(n/2)+cn, by applying the master theorem we have the complexity following
# The worst case complexity is O(nlogn) where n is the length of L


## Question 4
# Return majority element of M if it exists, otherwise 'False'.
# The worst-case run time is:
# Because:
def getMajorityInMatrixDaC(M):

    def helpGetMajorityDaC(rowStart, rowStop, colStart, colStop):
        # Here we apply the similar idea as in getMajorityDaC
        if (rowStop - rowStart == 1) and (colStop - colStart == 1):
            return M[rowStart][colStart]
        # Divide and conquer part
        rowMid = (rowStart + rowStop) // 2
        colMid = (colStart + colStop) // 2
        left_Majority = helpGetMajorityDaC(rowStart, rowMid, colStart, colMid)
        right_Majority = helpGetMajorityDaC(rowStart, rowMid, colMid, colStop)
        if left_Majority == right_Majority:
            return left_Majority
        left_MajorityFreq = getFrequencyFromMatrix(left_Majority, M, rowStart,
                                                   rowStop, colStart, colStop)
        right_MajorityFreq = getFrequencyFromMatrix(right_Majority, M,
                                                    rowStart, rowStop,
                                                    colStart, colStop)
        if left_MajorityFreq > ((rowStop - rowStart) *
                                (colStop - colStart)) // 2:
            return left_Majority
        if right_MajorityFreq > ((rowStop - rowStart) *
                                 (colStop - colStart)) // 2:
            return right_Majority
        return False

    return helpGetMajorityDaC(0, len(M), 0, len(M[0]))


# Question 4 Answer
# The algorithms implemented in question 4 which is exactly the same with in quesiton 3
# Since the size of the matrix which is n=2^k*2^k, Therefore, the complexity of the algorithm is O(nlogn) where n is the size of the matrix


# Returns the frequency of v in M[rowStart:rowStop][colStart:colStop].
def getFrequencyFromMatrix(v, M, rowStart, rowStop, colStart, colStop):
    freq = 0
    for row in range(rowStart, rowStop):
        freq += getFrequency(v, M[row], colStart, colStop)
    return freq


## Question 5
# Return majority element of L if it exists, otherwise 'False'.
# The worst-case run time is:
# Because:
def getMajorityBoyerMoore(L):
    # initialization
    freq = 0
    curr = None
    # list all the elements in the lis
    for el in L:
        if freq == 0:
            curr = el
            freq = 1
        elif el != curr:
            freq -= 1
        else:
            freq += 1
    # justify whether curr is the majority of list or not
    if getFrequency(curr, L, 0, len(L)) > len(L) // 2:
        return curr
    return False


# Question 5 Answer
# For the first part of the algorithms, we have to view all the elements in the list which gave us the complexity of C(n)
# For the second part we check whether is majority, which in the wrost case we have C(n) computation
# Therefore we have the complexity that 2C(n) = O(n)


## Question 6
# Return majority element of L with probability at least p if it exists, otherwise 'False'.
# Probability for one try finding the existing majority element is at least:
# Probability that m tries all fail (assuming a majority element exists) is at most:
def getMajorityRandomized(L, p):
    m = getMajorityBoyerMoore(L)
    # here we compute the freq of majority element
    num = 0
    for i in range(len(L)):
        if L[i] == m:
            num += 1
    freq = num / len(L)
    # with the formula we have freq^times >= p then times >= log(p)/log(freq)
    times = 0
    if p > 0 and freq != False:
        times = int(log(p) / log(freq))
    # apply the randomized algorithm
    for i in range(times):
        if getMajorityBoyerMoore(L) != m:
            return False
    return m


# Question 6 Answer
"""
1. For the as least probability that randomized approach
We assume that the frequency of majority is 1/2, which means there are n/2 majority appears in the list.
by uniform random selection which we have the probability to get the right majority P >= 1/2 since the number of majority is at least n/2

2. at most the probability that m ≥ 1 independent tries of this randomized approach all incorrectly return False
For the similar reason, for a single trial the probability of failed is P<=1/2
Since all the m times trials are independent, therefore we have P(m times all falied) <= (1/2)^m
Then the at most probability is (1/2)^m
"""
