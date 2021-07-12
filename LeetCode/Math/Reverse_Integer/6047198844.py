class Solution:
    def reverse(self, x: int) -> int:
        #부호값이 정해지지 않은 답.
        ans = int(str(abs(x))[::-1])
        if ans == 0 or ans < -2**31 or ans > 2**31 - 1:
            return 0
        return x // abs(x) * ans