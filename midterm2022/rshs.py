from random import randint, uniform


## Question 7
# Return a bit string of length n uniformly at random from {0, 1}^n.
def createBitStringUniformly(n):
    lis = [0] * n
    for i in range(n):
        lis[i] = randint(0, 1)
    return lis


## Question 8
# Return a new bit string that performed single-bit flip mutation on a copy of x.
def singleBitFlip(x):
    lis = x.copy()
    pos = randint(0, len(lis) - 1)
    lis[pos] = 1 - lis[pos]
    return lis


## Question 9
# Return a new bit string that performed standard bit mutation on a copy of x.
# Expected number of different bits between x and the mutant:
def standardBitMutation(x):
    # standard bit mutation
    lis = x.copy()
    n = len(lis)
    for i in range(n):
        if uniform(0, 1) < 1 / n:
            lis[i] = 1 - lis[i]
    return lis


# Question 9 Answer
"""
Since we have to view all the element in the list, the list is with length n. And for each node
we have a probability 1/n that whether we flip or not. Therefore if we assume the the length of n
is large enough, we have the expectation number for 1 element that flip by the Law of Large number 
theorem. as n tend to infinity, we have E[number of flip] = n * 1/n = 1 by large number theorem.
"""


## Question 10
# Return a tuple (x, it), where x is the best solution found and it is the number of iterations.
def rsh(n, f, terminated, mutation):
    x = createBitStringUniformly(n)
    it = 0
    while not terminated(it):
        x = mutation(x)
        it += 1
    return (x, it)


## Question 11
# (1 + 1) EA on OneMax (on n bits)
#    Pr[A_i] ≥
#    Expected run time is at most:
#
# RLS on LeadingOnes (on n bits)
#    Pr[A_i] =
#    Expected run time is at most:
