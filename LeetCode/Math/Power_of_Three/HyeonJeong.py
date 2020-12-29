class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while (n % 3) == 0: # 3으로 나눠지는 경우에만 계속 나눠서 1이 될때까지
            n /= 3
        if n == 1:
            return True
        return False