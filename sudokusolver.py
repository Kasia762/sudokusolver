import matplotlib.pyplot as plt
import numpy as np

class solveSudoku:
    ''' Class to solve sudoku board
        Parameters:
            board (array): unsolved sudoku
        Returns:
            solution (array): solved sudoku
    '''
    pass
    def __init__(self,board,empty):
        self.board=board
        self.empty=empty
        self.solve(self.board)
        
    def emptySpaces(self,board):
        for row in range(9):
            for col in range(9):
                if board[row][col]==self.empty:
                    return(row, col)
        return None
    def valid(self,board, num, pos):
        #rows
        for col in range(9):
            if board[pos[0]][col]==num and pos[1]!=col:
                return False
        #columns
        for row in range(9):
            if board[row][pos[1]] == num and pos[0] != row:
                return False
        #small 3x3 board box
        box_row = pos[0] // 3
        box_col = pos[1] // 3
        for row in range(box_row*3, box_row*3 + 3):
            for col in range(box_col*3, box_col*3 + 3):
                if board[row][col] == num and (row, col) != pos:
                    return False
        return True

    def solve(self, board):
        find=self.emptySpaces(self.board)
        if not find:
            return True
        else:
            row, col=find
        for num in range(1,10):
            if self.valid(self.board, num, (row,col)):
                self.board[row][col]=num
                if self.solve(self.board):
                    return True
            self.board[row][col] = self.empty
        return False
    
    def solution(self):
        return self.board