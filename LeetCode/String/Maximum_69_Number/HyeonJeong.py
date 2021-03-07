class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i, n in enumerate(str(num)):
            if n == '6':
                return s[:i] + '9' + s[i+1:]
        return s
