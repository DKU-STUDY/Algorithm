class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        res = list()
        for i in range(len(n),0,-3):
            if i - 3 >= 0:
                res.append(n[i-3:i])
            else:
                res.append(n[0:i])
        return ".".join(res[::-1])