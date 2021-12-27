class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == min(matrix[y]) and matrix[y][x] == max(list(zip(*matrix))[x]):
                    res.append(matrix[y][x])
        return res