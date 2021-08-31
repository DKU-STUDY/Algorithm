class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 첫번째 행과 열로 0을 표현하자. -> 행의 첫번째에 0이있으면 그 행은 0으로 칠해져야한다는뜻이다.
        # 표현하는것은 좋다. 하지만 해당 행 자체가 0이였다면 -> 값이 왜곡되게 된다. flag로 표현한다.
        # 행의 첫번째나 열의 첫번째는 접근의 맨처음이므로 더렵혀지지않는다 -> 제대로된 flag를 가질수있다.
        # fr/fc는 순수 값이 0일때를 뜻한다. 0일때 True를가진다.
        fr = False
        fc = False

        m = len(matrix)
        n = len(matrix[0])

        # 첫번째 행과 열을 0으로 칠하자.
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # flag값 먼저 챙기자.
                    if i == 0: fr = True
                    if j == 0: fc = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 첫번째 행과 열이 0일 경우 칠하기. 이때 범위에 유의한다.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # flag값에 따른 첫번째 row / column칠하기
        if fc:
            for i in range(m):
                matrix[i][0] = 0

        if fr:
            for j in range(n):
                matrix[0][j] = 0

