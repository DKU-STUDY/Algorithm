class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        begin = 0
        end = m * n - 1

        while begin <= end:
            mid = (begin + end) // 2
            search = matrix[mid // n][mid % n]
            if search < target:
                begin = mid + 1
            elif search > target:
                end = mid - 1
            else:
                return True

        return False