class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        copy_matrix = copy.deepcopy(matrix)
        for c in range(n):
            for r in range(n):
                matrix[r][c]= copy_matrix[n-c-1][r]
