# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        begin = 1
        end = n

        while begin < end:
            num = (begin + end) // 2
            if guess(num) == -1:
                end = num - 1
            elif guess(num) == +1:
                begin = num + 1
            else:
                return num
        return begin