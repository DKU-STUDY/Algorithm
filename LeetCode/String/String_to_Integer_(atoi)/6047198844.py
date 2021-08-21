class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = ""
        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]

        res = sign + "0"
        for n in s:
            if n.isdigit():
                res += n
            else:
                break

        res = int(res)

        min_value = -2 ** 31
        max_value = 2 ** 31 - 1

        if res < min_value:
            return min_value
        if res > max_value:
            return max_value
        return res
