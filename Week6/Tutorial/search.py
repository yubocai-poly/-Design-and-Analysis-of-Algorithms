# -*- coding: utf-8 -*-

### For comparing strings


def string_compare(P, S):
    for j in range(len(P)):
        if not P[j] == S[j]:
            return False
    return True


### naive string matcher
# Question 1
def string_match(T, P):
    m = len(P)
    n = len(T)

    position = []
    for i in range(n - m + 1):
        if string_compare(P, T[i:i + m]):
            position.append(i)
    return position


### number of characters
base = 256

### karp_rabin_sum


# Question 2
def hash_string_sum(S):
    m = len(S)
    hash_sum = 0
    for i in range(m):
        hash_sum += ord(S[i])
    return hash_sum


# Question 3
def hash_string_sum_update(h, Ti, Tim):
    return h - ord(Ti) + ord(Tim)


# Question 4
def karp_rabin_sum(T, P):
    m = len(P)
    n = len(T)
    num_false = 0
    position = []
    hp = hash_string_sum(P)
    ht = hash_string_sum(T[0:m])

    for i in range(n - m + 1):
        if hp == ht:
            if string_compare(P, T[i:i + m]):
                position.append(i)
            else:
                num_false += 1
        if i < n - m:
            ht = hash_string_sum_update(ht, T[i], T[i + m])

    return position, num_false


### karp_rabin_mod


# Question 5
def hash_string_mod(S, q):
    m = len(S)
    hash_sum = 0
    for i in range(m):
        hash_sum = (base * hash_sum + ord(S[i])) % q  # by apply Horner's rule
    return hash_sum


def hash_string_mod_update(h, q, Ti, Tim, dm):
    return (base * (h - dm * ord(Ti)) + ord(Tim)) % q


def karp_rabin_mod(T, P, q):
    n = len(T)
    m = len(P)
    num_false = 0
    position = []
    hp = hash_string_mod(P, q)
    ht = hash_string_mod(T[0:m], q)

    for i in range(n - m + 1):
        if hp == ht:
            if string_compare(P, T[i:i + m]):
                position.append(i)
            else:
                num_false += 1
        if i < n - m:
            ht = hash_string_mod_update(ht, q, T[i], T[i + m], base**(m - 1))

    return position, num_false
