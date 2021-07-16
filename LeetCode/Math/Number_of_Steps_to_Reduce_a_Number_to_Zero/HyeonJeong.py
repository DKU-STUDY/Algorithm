class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while (num != 0) :
            cnt += 1
            if num % 2 == 0:
                num /= 2
                continue
            num -= 1
        return cnt
