class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while 1:
            m = 0
            if len(s) == 1:
                return int(s)
            for i in s:
                m += int(i)
            s = str(m)

# addDigits(38) == 2
# 38 -> 3 + 8 = 11 -> 1 + 1 = 2