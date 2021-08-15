class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        res = 0
        cnt = 1
        ndivisor = divisor
        while dividend >= ndivisor:
            dividend -= ndivisor
            res += cnt
            # 2배
            cnt <<= 1
            ndivisor <<= 1

        res += self.divide(dividend, divisor)

        if positive == False:
            res = -res

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        return 2 ** 31 - 1