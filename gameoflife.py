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

	def get_neighbors(self, subArray, cell_value):
		neighbors = np.sum(subArray)
		return neighbors - 1 if cell_value else neighbors

def rand_board(board):
	board.board = np.random.randint(0, 2, (board.length, board.width))

def print_cell(win, board):
	win.fill(BLACK)
	for y in range(0, board.length):
		for x in range(0, board.width):
			if board.board[y][x] == 1:
				pygame.draw.rect(win, WHITE, pygame.Rect(x * SIZE + 1, y * SIZE + 1, SIZE - 2, SIZE - 2))

def next_cycle(board):
	tmp = board.__copy__()

	for y in range(0, tmp.length):
		for x in range(0, tmp.width):
			array = tmp.board[max(y - 1, 0):min(y + 2, tmp.length), max(x - 1, 0):min(x + 2, tmp.width)]
			neighbors = tmp.get_neighbors(array, tmp.board[y][x])
			if (not(neighbors == 2 or neighbors == 3)):
				board.board[y][x] = 0
				continue
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
			elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
				mouse = pygame.mouse.get_pos()
				if pygame.mouse.get_pressed()[0]:
					board.board[mouse[1] // SIZE][mouse[0] // SIZE] = 1
				elif pygame.mouse.get_pressed()[2]:
					board.board[mouse[1] // SIZE][mouse[0] // SIZE] = 0
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
			manual_cycle = False
			#pygame.time.wait(DELAY)
		pygame.display.flip()

def main():
	pygame.init()
	pygame.display.set_caption("Game Of Life")
	win = pygame.display.set_mode((WIDTH * SIZE, LENGTH * SIZE))
	start_rendering(win)

if __name__ == '__main__':
	main()
