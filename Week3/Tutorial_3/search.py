# -*- coding: utf-8 -*-
# CSE202 - Design and Analysis of Algorithms
# Author: Yubo Cai
# Date: 2022-10-06

import math


def binary_search_rec(A, v, left, right):
    if (right >= left):
        mid = left + (
            right - left
        ) // 2  # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A, v, left, mid - 1)
        else:
            return binary_search_rec(A, v, mid + 1, right)

    return -1


## Q1 - Binary Search ##
def binary_search(A, v):
    # we cab see that the  interative version of code run faster compare with the recursive version
    n = len(A)
    left = 0
    right = n - 1
    while (right >= left):
        mid = left + (right - left) // 2
        if v == A[mid]:
            return mid
        if v < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def cost_binary_search(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return cost_binary_search((n + 1) // 2) + 3


## Q2 - Ternary Search 三元搜索算法 ##
def ternary_search(A, v):
    n = len(A)
    l = 0
    r = n - 1
    while (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if v == A[mid1]:
            return mid1
        if v == A[mid2]:
            return mid2
        if v < A[mid1]:
            r = mid1 - 1
        if v > A[mid2]:
            l = mid2 + 1
        if v > A[mid1] and v < A[mid2]:
            l = mid1 + 1
            r = mid2 - 1
    return -1


def cost_ternary_search(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return cost_ternary_search((n + 2) // 3) + 5


def cost_binary_search_real(A, v):
    if len(A) == 0: return 0

    left = 0
    right = len(A) - 1
    cost = 0
    while (right >= left):
        cost += 1  # <-- This was also missing!!
        mid = left + (right - left) // 2
        if (v == A[mid]):
            return cost + 1
        elif (v < A[mid]):
            right = mid - 1  # <-- The bug was here
            cost += 2  #     used to be just `return cost + 2`
        else:
            left = mid + 1
            cost += 2

    return cost


def cost_ternary_search_real(A, v):
    if len(A) == 0:
        return 0

    left = 0
    right = len(A) - 1
    cost = 0
    while (right >= left):
        cost += 1
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if (v == A[mid1]):
            return cost + 1
        if v == A[mid2]:
            return cost + 1
        elif (v < A[mid1]):
            right = mid1 - 1
            cost += 3
        elif (v > A[mid2]):
            left = mid2 + 1
            cost += 4
        else:
            left = mid1 + 1
            right = mid2 - 1
            cost += 4
    return cost


## Q3 - Exponential Search 指数搜索 ##
def binary_search_2(A, v, left, right):
    # we cab see that the  interative version of code run faster compare with the recursive version
    n = len(A)
    while (right >= left):
        mid = left + (right - left) // 2
        if v == A[mid]:
            return mid
        if v < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def exponential_search(A, v):
    # we can't use the recursive version of code to solve this problem
    if len(A) == 0:
        return -1
    if len(A) == 1:
        if A[0] == v:
            return 0
        else:
            return -1

    n = len(A)
    # here we first try to find the right
    right_index = 1
    while (right_index < n) and (A[right_index] < v):
        right_index *= 2
    left = right_index // 2
    return binary_search_2(A, v, left, min(right_index, n - 1))


def cost_exponential_search(v):
    if v == 0:
        return 0
    return int(math.log(v, 2)) + cost_binary_search(v - int(math.log(v, 2)))


## Q4 - Interpolation Search 插值搜索 ##
def interpolation_search(A, target):

    # base case
    if len(A) == 0:
        return -1

    # search space is A[left…right]
    (left, right) = (0, len(A) - 1)

    while A[right] != A[left] and A[left] <= target <= A[right]:

        # estimate mid
        mid = left + (target - A[left]) * (right - left) // (A[right] -
                                                             A[left])

        # key is found
        if target == A[mid]:
            return mid
        # discard all elements in the right search space, including the middle element
        elif target < A[mid]:
            right = mid - 1
        # discard all elements in the left search space, including the middle element
        else:
            left = mid + 1

    if target == A[left]:
        return left

    return -1


## Q6 Building on Binary Search ##
def findFirstOccurrence(A, v):
    # we cab see that the  interative version of code run faster compare with the recursive version
    n = len(A)
    left = 0
    right = n - 1
    while (right >= left):
        mid = left + (right - left) // 2
        if v == A[mid]:
            while (mid > 0) and (A[mid - 1] == v):
                mid -= 1
            return mid
        if v < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def findLastOccurrence(A, v):
    # we cab see that the  interative version of code run faster compare with the recursive version
    n = len(A)
    left = 0
    right = n - 1
    while (right >= left):
        mid = left + (right - left) // 2
        if v == A[mid]:
            while (mid > 0) and (A[mid + 1] == v):
                mid += 1
            return mid
        if v < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


## Q7 ##
def findbinaryposition(A, v):
    # We use a aux function to find the binary position of v in A
    left, right = 0, len(A) - 1

    while left <= right:
        middle = (left + right) // 2

        if A[middle] < v:
            left = middle + 1
        elif A[middle] > v:
            right = middle - 1
        else:
            return middle
    return right + 1


def findKClosestElements(A, v, k):
    position = findbinaryposition(A, v)
    result = []
    left, right = position - 1, position
    while k > 0:
        if left < 0:
            result.append(A[right])
            right += 1
        elif right >= len(A):
            result.append(A[left])
            left -= 1
        elif abs(A[left] - v) <= abs(A[right] - v):
            result.append(A[left])
            left -= 1
        else:
            result.append(A[right])
            right += 1
        k -= 1

    return sorted(result)


print(findKClosestElements([0, 2, 5, 7, 8, 11, 15], 20, 2))
print(findKClosestElements([0, 2, 5, 7, 8, 11, 15], 6, 4))


## Q8 ##
def findFrequency(A):
    # 这个算法相当于我们每次找到了A[left]==A[right]的时候，我们就把中间所有的数字都加到result里面
    # 然后把left赋值给right+1， right放到len(A)-1的位置重新再来一次
    dict = {}
    left = 0
    right = len(A) - 1
    while left <= right:
        if A[left] == A[right]:
            dict[A[left]] = dict.get(A[left], 0) + (right - left + 1)
            left = right + 1
            right = len(A) - 1
        else:
            right = (left + right) // 2

    return dict


print(findFrequency([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]))
