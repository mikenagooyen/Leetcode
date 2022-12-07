# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     1. Each row must contain the digits 1-9 without repetition.
#     2. Each column must contain the digits 1-9 without repetition.
#     3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

# Use a hashset for checking rows and cols duplicate numbers
# We can use row/3 and col/3 for finding index of a 3x3 sub square
# 
from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subsquare = collections.defaultdict(set) # key = (r/3, c/3)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or # check if current number is in the row
                    board[row][col] in cols[col] or # check if current number is in the col
                    board[row][col] in subsquare[(row // 3, col // 3)]): # check if the current number is in the 3x3 sub square
                    return False
                # update all sets to append the value
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                subsquare[(row//3, col//3)].add(board[row][col])
        return True

obj = Solution()
board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(obj.isValidSudoku(board))