class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        board =[[] for _ in range(numRows)]
        
        step = numRows - 1
        cur_row = 0
        cur_col = 0
        #s.length, numRows -> 최대 1000 이므로 브루트포스
        for char in s:
            #일직선
            if cur_col % step == 0:
                board[cur_row].append(char)
                cur_row += 1
                if cur_row == step:
                    cur_col += 1
            #우상으로
            else:
                cur_row -= 1
                cur_col += 1
                board[cur_row].append(char)
                                
        print(board)