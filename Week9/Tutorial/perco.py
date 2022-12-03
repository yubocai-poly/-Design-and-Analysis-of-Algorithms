# -*- coding: utf-8 -*-
# CSE202 - Disign and Analysis of Algorithms
# Percolation on a square grid 渗透问题

from uf import Rank_UF

import random


def draw_grid(grid, N):
    for ii in range(N):
        i = ii + 1
        for j in range(N):
            if grid[i][j] == 0:
                print('X', end='')
            else:
                print(' ', end='')
        print()


def pos_to_int(N, i, j):
    return N * i + j


# Question 4
def get_vacant_neighbors(G, N, i, j):
    '''
    TO IMPLEMENT
    '''
    res = []
    for k in [-1, 1]:
        if G[i + k][j] == 1:
            res.append([i + k, j])

    if j > 0 and G[i][j - 1] == 1:
        res.append([i, j - 1])
    if j < N - 1 and G[i][j + 1] == 1:
        res.append([i, j + 1])

    return res


# Question 5
def make_vacant(UF, G, N, i, j):
    '''
    TO IMPLEMENT
    '''
    G[i][j] = 1
    for pos in get_vacant_neighbors(G, N, i, j):
        UF.union(pos_to_int(N, i, j), pos_to_int(N, pos[0], pos[1]))


# Question 6
def ratio_to_percolate(N):
    '''
    TO IMPLEMENT
    '''
    # Generate an (N+2) x N grid
    rows = N + 2
    grid = []
    for i in range(rows):
        grid.append([0] * N)
    uf = Rank_UF(rows * N)

    # Initialize the top and bottom rows
    for i in range(N):
        grid[0][i] = 1
        grid[N + 1][i] = 1
        if i > 0:
            uf.union(pos_to_int(N, 0, 0), pos_to_int(N, 0, i))
            uf.union(pos_to_int(N, N + 1, 0), pos_to_int(N, N + 1, i))

    # Initialize the left and right columns
    top = pos_to_int(N, 0, 0)
    bottom = pos_to_int(N, N + 1, 0)
    count = 0
    while not uf.is_connected(top, bottom):
        i, j = random.randint(1, N), random.randint(0, N - 1)
        if grid[i][j] == 0:
            make_vacant(uf, grid, N, i, j)
            count += 1

    return count / (N * N)