# import libraries
import numpy as np


# create a class for the Sudoku puzzle
class Sudoku:

    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.box_size = int(np.sqrt(self.size))

    # check if a number is valid in a given position
    def valid(self, row, col, num):
        # check row
        if num in self.board[row]:
            return False
        # check column
        if num in self.board[:, col]:
            return False
        # check box
        box_row = (row // self.box_size) * self.box_size
        box_col = (col // self.box_size) * self.box_size
        if num in self.board[box_row:box_row + self.box_size, box_col:box_col + self.box_size]:
            return False
        return True

    # solve the puzzle recursively
    def solve(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    for num in range(1, self.size + 1):
                        if self.valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True


# create a sample puzzle
board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# solve the puzzle
game = Sudoku(board)
game.solve()

# print the solved puzzle
print(game.board)
# -*- coding: utf-8 -*-
"""
Date Created: 01/04/2023 - 11:10:26
@Author: aathi

File Name: sudoku.py
"""
