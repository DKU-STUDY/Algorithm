class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m-1개의 '아래'와 n-1개의 '오른쪽'의 순서를 정하는 순열
        num = 1 # num은 nCr에서 n!
        for i in range(2,m+n-1):
            num *= i
        r1 = 1 #r1은 nCr에서 r!
        r2 = 1 #r2는 nCr에서 (n-r)!
        for i in range(2, m):
            r1 *= i
        for i in range(2, n):
            r2 *= i
        return num//(r1*r2)
