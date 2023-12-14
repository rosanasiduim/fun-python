import numpy as np
import random

def generate_sudoku_square():
     # Create an empty 3x3 square
     square = np.zeros((3, 3), dtype=int)

     # Fill the square with random values
     numbers = list(range(1, 10))
     random.shuffle(numbers)

     index = 0
     for i in range(3):
         for j in range(3):
             square[i, j] = numbers[index]
             index += 1

     return square

def shuffle_sudoku_square(square):
     # Shuffle the lines inside the square
     np.random.shuffle(square)

     # Shuffle the columns inside the square
     square = square.transpose()
     np.random.shuffle(square)

     return square

def print_sudoku(square):
     for row in square:
         print(" ".join(map(str, row)))

def generate_sudoku():
     # Generate an empty 9x9 board
     board = np.zeros((9, 9), dtype=int)

     # Fill the board with 3x3 squares
     for i in range(0, 9, 3):
         for j in range(0, 9, 3):
             square = generate_sudoku_square()
             square = shuffle_sudoku_square(square)
             board[i:i+3, j:j+3] = square

     return board

if __name__ == "__main__":
     sudoku_board = generate_sudoku()
     print("Generated Sudoku Board:")
     print_sudoku(sudoku_board)
