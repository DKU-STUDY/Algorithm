class Solution:
    def is_column_valid(self, board):
        for column in zip(*board):
            if not self.is_unit_valid(column):
                return False
        return True
            
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    def is_square_valid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[y][x] for x in range(j,j+3) for y in range(i,i+3)]
                if not self.is_unit_valid(square):
                    return False
        return True
        
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_column_valid(board) and 
                self.is_row_valid(board) and 
                self.is_square_valid(board))