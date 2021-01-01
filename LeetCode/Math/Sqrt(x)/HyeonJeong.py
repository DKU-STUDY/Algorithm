class Solution:
    def mySqrt(self, x: int) -> int:
        n = sqrt(x)
        if n != int(n):
            return floor(n) #제곱근이 정수가 아닐 경우는 내림
        return int(n)
