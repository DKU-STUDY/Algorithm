class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while n > (4 ** i):
            i += 1
        return n == (4 ** i)
