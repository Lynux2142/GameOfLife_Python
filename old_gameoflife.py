#!/usr/bin/python2.7

import numpy as np
from graphics import *

WIDTH = 10
LENGTH = 10
SIZE = 100

class Game:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.board = np.zeros((length, width))
        for y in range(0, self.length):
            for x in range(0, self.width):
                self.board[y][x] = np.random.randint(2, size=1)

    def __copy__(self):
        copy = Game(self.width, self.length)
        copy.board = np.copy(self.board)
        return copy

    def get_neighbors(self, x, y):
        neighbors = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (not(j == 0 and i == 0) and (x + i) >= 0 and (y + j) >= 0 and (x + i) < self.width and (y + j) < self.length):
                    if (self.board[y + j][x + i] == 1):
                        neighbors = neighbors + 1
        return neighbors


def next_cycle(board):
    tmp = board.__copy__()

    for y in range(0, tmp.length):
        for x in range(0, tmp.width):
            neighbors = tmp.get_neighbors(x, y)
            if (tmp.board[y][x] == 1):
                if (not(neighbors == 2 or neighbors == 3)):
                    board.board[y][x] = 0
            else:
                if (neighbors == 3):
                    board.board[y][x] = 1

def main():
    board = Game(WIDTH, LENGTH)
    win = GraphWin("Game Of Life", WIDTH * SIZE, LENGTH * SIZE)
    win.setBackground('black')
    while (1):
        for y in range(0, board.length):
            for x in range(0, board.width):
                rect = Rectangle(Point(x * SIZE, y * SIZE), Point(x * SIZE + SIZE + 1, y * SIZE + SIZE + 1))
                if board.board[y][x] == 1:
                    rect.setFill('white')
                    rect.draw(win)
                else:
                    rect.setFill('black')
                    rect.draw(win)
        next_cycle(board)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
