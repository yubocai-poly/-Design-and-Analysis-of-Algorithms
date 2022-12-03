# -*- coding: utf-8 -*-
from uf import Rank_UF
import random


class Hex:

    def __init__(self, N):
        # size of the board (counting extra rows / columns)
        self.size = N + 2
        # initialisation of the board (all hexagons are free)
        self.board = [[0 for j in range(self.size)] for i in range(self.size)]

        # initialisation of the Union-Find object
        nelem = self.size**2
        self.uf = Rank_UF(nelem)

        # first player to play is player 1
        self.player = 1

        l = self.size - 1
        # union of sides of each player
        # player 1 is affected to the extra rows, player 2 extra columns
        for i in range(1, self.size - 1):
            self.board[0][i] = 1
            self.board[l][i] = 1
            self.board[i][0] = 2
            self.board[i][l] = 2

            if i > 0:
                self.uf.union(self.hex_to_int(1, 0), self.hex_to_int(i, 0))
                self.uf.union(self.hex_to_int(1, l), self.hex_to_int(i, l))

                self.uf.union(self.hex_to_int(0, 1), self.hex_to_int(0, i))
                self.uf.union(self.hex_to_int(l, 1), self.hex_to_int(l, i))

        # get the indices in UF of the bottom and top sides of each player
        self.bot1 = self.hex_to_int(0, 1)
        self.top1 = self.hex_to_int(l, 1)
        self.bot2 = self.hex_to_int(1, 0)
        self.top2 = self.hex_to_int(1, l)

    def hex_to_int(self, i, j):
        return i * (self.size) + j

    def print_board(self):
        for i in range(1, self.size - 1):
            print(' ' * (i - 1), end='')
            for j in range(1, self.size - 1):
                if self.board[i][j] == 0:
                    print('_', end='')
                if self.board[i][j] == 1:
                    print('X', end='')
                if self.board[i][j] == 2:
                    print('O', end='')
            print()

    # Question 7
    def neighbours(self, i, j):
        '''
        TO IMPLEMENT
        computes and returns the list of the hexagons that are neighbors of the hexagon at position (i, j) and belong to
        the current player.
        '''
        res = []
        # We add all the neighbours of the hexagon (i,j) to the list of neighbours, and then we justify if they are the we try to find or not
        neighbors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1],
                     [i - 1, j + 1], [i + 1, j - 1]]
        for neighbor in neighbors:
            # if the neighbor is in the board and if the neighbor is of the current player, then we add it to the list of result
            if self.board[neighbor[0]][
                    neighbor[1]] == self.player and 0 <= neighbor[
                        0] <= self.size - 1 and 0 <= neighbor[
                            1] <= self.size - 1:
                res.append(neighbor)

        return res

    # Question 8
    def is_game_over(self):
        '''
        TO IMPLEMENT
        '''
        if (self.player == 1):
            if (self.uf.is_connected(self.bot1, self.top1)):
                print("Player 1 wins")
                return True
            return False
        else:
            if (self.uf.is_connected(self.top2, self.bot2)):
                print("Player 2 wins")
                return True
            return False

    # Question 9
    def random_turn(self):
        '''
        TO IMPLEMENT
        '''
        x, y = random.randint(1,
                              self.size - 2), random.randint(1, self.size - 2)
        while (self.board[x][y] != 0):
            x, y = random.randint(1, self.size - 2), random.randint(
                1, self.size - 2)
        self.board[x][y] = self.player
        for neighbor in self.neighbours(x, y):
            self.uf.union(self.hex_to_int(x, y),
                          self.hex_to_int(neighbor[0], neighbor[1]))

    # Question 10
    def random_play(self):
        '''
        TO IMPLEMENT
        '''
        num_turns = 0
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

        while (not self.is_game_over()):
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.random_turn()

        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if self.board[i][j] != 0:
                    num_turns += 1

        return num_turns / ((self.size - 2)**2)


# Test
N = 6
h = Hex(N)
print(h)
h.board[2][2] = 1
h.board[2][3] = 2
E = [[1, 2], [2, 1], [3, 2], [1, 3], [3, 1]]
for p in E:
    h.board[p[0]][p[1]] = 1
h.print_board()
