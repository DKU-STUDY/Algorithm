class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        
        for step in range((N+1)//2):
            for d in range(N-2*step-1):
                matrix[step][step+d],matrix[step+d][N-1-step], matrix[N-1-step][N-1-step-d], matrix[N-1-step-d][step] = matrix[N-1-step-d][step], matrix[step][step+d], matrix[step+d][N-1-step], matrix[N-1-step][N-1-step-d]
                
                
        
'''

a = matrix[step][step+d]
b = matrix[step+d][N-1-step]
c = matrix[N-1-step][N-1-step-d]
d = matrix[N-1-step-d][step]

N = 3
00 01 02
10 11 12
20 21 22


N = 4
00  01  02  03
10  11  12  13
20  21  22  23
30  31  32  33
'''