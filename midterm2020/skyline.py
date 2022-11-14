# -*- coding: utf-8 -*-
# CSE202 - Design and Algorithms Analysis
# Midterm 2020
# Author: Yubo Cai

# the input is represented by a list of (left,height,right)
# the output (skyline) is represented by an ordered list of (left,height) and always ends with
# a (left,0) entry


def rects_height_at(rects, x):
    """
    given a list of rectangles and a position, return h(x)=max{y:(l,r,y) in rects and l<=x<r}
    note that the inequality l<=x<r is assymetric: large on the left and strict on the right
    """
    max_height = 0
    for el in rects:
        if el[0] <= x and x < el[2]:
            max_height = max(max_height, el[1])
    return max_height


def simplify_skyline(skyline):
    """simplify a skyline by removing redundant entries"""
    res = []
    j = 0
    for i in range(len(skyline)):
        if skyline[j][1] != skyline[i][1]:
            res.append(skyline[j])
            j = i
    if skyline[-1][1] != res[-1][1]:
        res.append(skyline[-1])
    return res


def skyline_naive(rects):
    """computes the skyline in O(n^2)"""
    coords = sorted(
        list(
            set([left for (left, _, _) in rects] +
                [right for (_, _, right) in rects])))
    return simplify_skyline([(x, rects_height_at(rects, x)) for x in coords])


def merge_skylines(sky1, sky2):
    """merge two skylines"""
    res = []
    h1 = 0
    h2 = 0
    i = 0
    j = 0
    while i < len(sky1) and j < len(sky2):
        if sky1[i][0] < sky2[j][0]:
            h1 = sky1[i][1]
            res.append((sky1[i][0], max(h1, h2)))
            i += 1
        elif sky1[i][0] > sky2[j][0]:
            h2 = sky2[j][1]
            res.append((sky2[j][0], max(h1, h2)))
            j += 1
        else:
            h1 = sky1[i][1]
            h2 = sky2[j][1]
            res.append((sky1[i][0], max(h1, h2)))
            i += 1
            j += 1
    res += sky1[i:]
    res += sky2[j:]

    return simplify_skyline(res)


def skyline_dac(rects):
    # we use divide and conquer to compute
    if len(rects) == 1:
        (left,h,right) = rects[0]
        return [(left,h),(right,0)]
    # divide and conquer
    n = len(rects) // 2
    sky1 = skyline_dac(rects[0:n])
    sky2 = skyline_dac(rects[n:])
    return merge_skylines(sky1, sky2)


sky1_red = [(1, 11), (2, 11), (3, 13), (5, 13), (7, 13), (9, 0), (12, 7),
            (14, 7), (16, 3), (19, 18), (22, 3), (23, 13), (24, 13), (25, 13),
            (28, 13), (29, 0)]
sky1 = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3),
        (23, 13), (29, 0)]

sky3 = [(1, 11), (5, 6), (7, 0), (12, 7), (16, 0), (19, 18), (22, 0), (24, 4),
        (28, 0)]
sky4 = [(3, 13), (9, 0), (14, 3), (23, 13), (29, 0)]

print(merge_skylines(sky3, sky4))