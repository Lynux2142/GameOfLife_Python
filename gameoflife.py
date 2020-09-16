#!/usr/local/bin/python3

import numpy as np
import pygame

WIDTH = 100
LENGTH = 100
SIZE = 10
DELAY = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.board = np.zeros((self.length, self.width))

    def __copy__(self):
        copy = Game(self.width, self.length)
        copy.board = np.copy(self.board)
        return copy

    def get_neighbors(self, array, cell_value):
        neighbors = np.sum(array)
        return neighbors - 1 if cell_value else neighbors

def rand_board(board):
    for y in range(0, board.length):
        for x in range(0, board.width):
            board.board[y][x] = np.random.randint(2, size=1)

def print_cell(win, board):
    for y in range(0, board.length):
        for x in range(0, board.width):
            if board.board[y][x] == 1:
                pygame.draw.rect(win, WHITE, pygame.Rect(x * SIZE + 1, y * SIZE + 1, SIZE - 2, SIZE - 2))
            else:
                pygame.draw.rect(win, BLACK, pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE))

def next_cycle(board):
    tmp = board.__copy__()

    for y in range(0, tmp.length):
        for x in range(0, tmp.width):
            array = tmp.board[max(y - 1, 0):max(y + 2, 0), max(x - 1, 0):max(x + 2, 0)]
            neighbors = tmp.get_neighbors(array, tmp.board[y][x])
            if (tmp.board[y][x] == 1):
                if (not(neighbors == 2 or neighbors == 3)):
                    board.board[y][x] = 0
            else:
                if (neighbors == 3):
                    board.board[y][x] = 1

def start_rendering(win):
    board = Game(WIDTH, LENGTH)
    running = True
    pause = False
    manual_cycle = False

    rand_board(board)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                board.board[mouse[1] // SIZE][mouse[0] // SIZE] = not board.board[mouse[1] // SIZE][mouse[0] // SIZE]
                print_cell(win, board)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rand_board(board)
                    print_cell(win, board)
                elif event.key == pygame.K_BACKSPACE:
                    board = Game(board.width, board.length)
                    print_cell(win, board)
                elif event.key == pygame.K_SPACE:
                    pause = not pause
                elif event.key == pygame.K_RIGHT:
                    manual_cycle = True
        if not pause or manual_cycle == True:
            next_cycle(board)
            print_cell(win, board)
            pygame.time.wait(DELAY)
        pygame.display.flip()
        manual_cycle = False

def main():
    pygame.init()
    pygame.display.set_caption("Game Of Life")
    win = pygame.display.set_mode((WIDTH * SIZE, LENGTH * SIZE))
    start_rendering(win)

if __name__ == '__main__':
    main()
