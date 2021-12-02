class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # 2로 나누기
        while n % 2 == 0:
            n //= 2

        # 3로 나누기
        while n % 3 == 0:
            n //= 3

        # 5로 나누기
        while n % 5 == 0:
            n //= 5

        return n == 1