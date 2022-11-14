# -*- coding: utf-8 -*-
# CSE202 - Design and Algorithms Analysis
# Midterm 2019
# Author: Yubo Cai


"""
Given a histogram, find the largest area of a rectangle contained in the
histogram.
"""
import math


# Question 5
def rect_from_left(hist, i):
    """compute max area of a rectangle [i,j] for all j, in linear time"""
    max_area = 0
    min_height = math.inf
    for j in range(i, len(hist)):
        min_height = min(hist[j], min_height)
        max_area = max(max_area, min_height * (j + 1 - i))

    return max_area


# Question 6
def rect_hist_brute(hist):
    """brute force (n^2) solution"""
    global_max = 0
    for i in range(len(hist)):
        global_max = max(global_max, rect_from_left(hist, i))
    return global_max


# Question 7
def expand_rect(H, i, j, left, right, h):
    """expand rectangle [l:r] to the left or the right, update height"""
    l1 = left
    r1 = right
    h1 = h
    if left == i:
        r1 = r1 + 1
        h1 = min(h, H[r1 - 1])
    if right == j:
        l1 = l1 - 1
        h1 = min(h, H[l1])
    if H[left - 1] > H[right]:
        l1 = l1 - 1
        h1 = min(h, H[l1])
    else:
        r1 = r1 + 1
        h1 = min(h, H[r1 - 1])
    return l1, r1, h1


# Question 8
def best_from_middle(hist, i, j, m):
    """compute max area of a rectangle that includes bar at position m"""
    left = m
    right = m + 1
    h = hist[m]
    max_area = h
    while left > i and right < j:
        left, right, h = expand_rect(hist, i, j, left, right, h)
        max_area = max(max_area, (right - left) * h)
    return max_area


# Question 9
def rect_hist_dac_aux(hist, i, j):
    """solve over interval [i,j)"""
    if i == j:
        return -math.inf
    m = (i + j) // 2
    # recursve on the left and right (both exclude the middle bar m)
    # NOTE clearly i < j thus i <= m so first interval makes sense
    # and similarly i + j < 2 * j thus m < j thus m+1 <= j
    max_area = max(rect_hist_dac_aux(hist, i, m),
                   rect_hist_dac_aux(hist, m + 1, j))
    return max(max_area, best_from_middle(hist, i, j, m))


def rect_hist_dac(hist):
    """divide-and-conquer (nlog(n)) solution"""
    return rect_hist_dac_aux(hist, 0, len(hist))
