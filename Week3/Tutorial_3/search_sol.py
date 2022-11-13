# -*- coding: utf-8 -*-

import math

def binary_search_rec(A,v,left,right):
    if (right >= left):
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A,v,left,mid-1)
        else:
            return binary_search_rec(A,v,mid+1,right)
    
    return -1
        
## Q1 ##
def binary_search(A,v):
    left = 0
    right = len(A) - 1
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return -1            

## Q1 ##
def cost_binary_search(n):
    if (n == 0):
        return 1
    elif (n == 1):
        return 4
    else:
        return cost_binary_search((n+1)//2) + 3
    
def cost_binary_search_real(A,v):
    if len(A) == 0: return 1

    left = 0
    right = len(A) - 1
    cost = 0
    while (right >= left):
        mid = left + int((right - left)/2)
        if (v == A[mid]):
            return cost + 2
        
        if (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1
        cost += 3

    return cost + 1
    
## Q2 ##
def ternary_search(A,v):
    left = 0
    right = len(A) - 1
    while (right >= left):
        shift = int((right - left)/3)
        mid1 = left + shift
        mid2 = right - shift
        if (A[mid1] == v):
            return mid1
        elif (A[mid2] == v):
            return mid2
        elif (v < A[mid1]):
            right = mid1 - 1
        elif (v < A[mid2]):
            right = mid2 - 1
            left = mid1 + 1
        else:
            left = mid2 + 1

    return -1

def cost_ternary_search(n):
    if (n == 0):
        return 1
    elif (n == 1):
        return 6
    else:
        return cost_ternary_search((n + 2)//3) + 5
    
def cost_ternary_search_real(A,v):
    if len(A) == 0: return 1

    left = 0
    right = len(A) - 1
    cost = 0
    while (right >= left):
        shift = (right - left)//3
        mid1 = left + shift
        mid2 = right - shift
        if (A[mid1] == v):
            return cost + 2
        elif (A[mid2] == v):
            return cost + 3
        elif (v < A[mid1]):
            right = mid1 - 1
            cost += 4
        elif (v < A[mid2]):
            right = mid2 - 1
            left = mid1 + 1
            cost += 5
        else:
            left = mid2 + 1
            cost += 5

    return cost + 1

## Q3 ##
def binary_search1(A,v,left,right):
    while left <= right:
        mid = left + (right - left)//2
        if v == A[mid]:
            return mid
        elif v < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def exponential_search(A,v):
    bound = 1
    while bound < len(A) and A[bound] < v:
        bound *= 2
    return binary_search1(A, v, bound//2, min(bound, len(A)))

def cost_exponential_search(v):
    return 2*math.ceil(math.log2(v)) + cost_binary_search(v//2)

## Q4 ##
def interpolation_search(A,v):
    if v < A[0] or v > A[-1]: return -1

    left = 0
    right = len(A) - 1
    while (right > left):
        mid = left + (v - A[left])*(right - left)//(A[right] - A[left])
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    if right == left and A[left] == v:
        return left

    return -1            

## Q6 ##
def findFirstOccurrence(A, v):
    left = 0
    right = len(A) - 1
    first = -1
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            first = mid

        if (v <= A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return first           

## Q6 ##
def findLastOccurrence(A, v):
    left = 0
    right = len(A) - 1
    last = -1
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            last = mid

        if (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return last           

## Q7 ##
def findKClosestElements(A, v, k):
    # Border cases (empty array or v outside)
    if len(A) == 0: return []
    if v < A[0]: return A[:k]
    if v > A[-1]: return A[-k:]

    # Do a binary search to find v or the insertion point
    left = 0
    right = len(A) - 1
    ind = -1
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            ind = mid
            break
        elif (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    # If v found (at ind) it will be the starting point
    # Otherwise, we have to choose the 1st closest neighbour
    if (ind == -1):
        if (v - A[right] < A[left] - v):
            ind = right
        else:
            ind = left

    # We will be now growing the interval 1-by-1 on either side
    # Left and right are the candidates for the next neighbour
    left, right = ind - 1, ind + 1

    # We already have the first element
    # so we only have to find k-1 more
    for _ in range(k-1):
        # if the left bound has been reached we can only expand to the right
        # it's ok to expand beyond the right bound - the slicing operator will 
        # take care of the overflow
        if left < 0:
            right += 1
        # symmetrically to for the right bound
        # it would not be ok to expand beyond 0, since A[-1] is the last element
        # however, we will not reach this branch if left < 0
        elif right >= len(A):
            left -= 1
        # if the bounds have not been reached, we can safeely choose
        # the closest among the two candidates
        elif (v - A[left] < A[right] - v):
            left -= 1
        else:
            right += 1
    
    # The right bound is excluded by the slicing operator
    # but we have to exclude the left one manually
    return A[left+1:right]

## Q7 ## Another version, which performs a binary search instead of a linear search for the k closest elements at the end
def findKClosestElements1(A, v, k):
    n = len(A)
    assert (k <= n), "Too many elements asked for."

    # Border cases (empty array or v outside)
    if len(A) == 0: return []
    if v < A[0]: return A[:k]
    if v > A[-1]: return A[-k:]

    # Do a binary search to find v or the insertion point
    left = 0
    right = len(A) - 1
    ind = -1
    while (right >= left):
        mid = left + (right - left)//2
        if (v == A[mid]):
            ind = mid
            break
        elif (v < A[mid]):
            right = mid - 1
        else:
            left = mid + 1

    # If v found (at ind) it will be the starting point
    # Otherwise, we have to choose the closest neighbor
    if (ind == -1):
        if (v - A[right] < A[left] - v):
            ind = right
        else:
            ind = left

    # Auxiliary function for computing the maximum distance within a range to a given value
    def largestDistance(leftBorder, rightBorder, valueToCompareAgainst):
        return max(valueToCompareAgainst - A[leftBorder], A[rightBorder] - valueToCompareAgainst)
    
    # Perform a binary search for the smallest index "left" such that A[left:left + k] contains A[ind] and such that the largest distance to v is minimized
    left = max(0, ind - k + 1)
    right = min(n - k, ind)
    while (True):
        leftDistance = largestDistance(left, left + k - 1, v)
        rightDistance = largestDistance(right, right + k - 1, v)
        if (leftDistance == rightDistance):
            return A[left:left + k]
        mid = left + (right - left)//2
        if (leftDistance < rightDistance):
            right = mid - (right == mid)
        else:
            left = mid + (left == mid)

## Q8 ##
def findFrequency(A):
 
    # dictionary to store the frequency of each element in the list
    freq = {}
 
    # search space is A[left:right+1]
    (left, right) = (0, len(A) - 1)
 
    # loop till the search space is exhausted
    while left <= right:
 
        # if A[left:right+1] consists of only one element, update its count
        if A[left] == A[right]:
            freq[A[left]] = freq.get(A[left], 0) + (right - left + 1)
 
            # now discard A[left:right+1] and continue searching in A[right+1:n]
            left = right + 1
            right = len(A) - 1
        else:
            # reduce the search space
            right = (left + right) // 2
 
    return freq

## Q8 ## Another version
def findFrequency1(A):
    freq = {}
    current = 0
    while (current < len(A)):
        left = current
        right = len(A) - 1
        v =  A[current]
        last = current
        while (right >= left):
            mid = left + (right - left)//2
            if (v == A[mid]):
                last = mid

            if (v < A[mid]):
                right = mid - 1
            else:
                left = mid + 1

        freq[v] = last - current + 1
        current = last + 1        

    return freq 







