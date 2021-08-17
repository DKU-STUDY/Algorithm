class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 더한다. -> 더한몫을 2로 나눈다. 나머지는 그 자리수가 되고 몫은 다음자리수로 넘어간다.
        AN = len(a)
        BN = len(b)
        N = max(AN, BN)
        res = ''
        rnd = 0

        for idx in range(1, N + 1):
            if idx <= AN and a[-idx] == '1':
                rnd += 1
            if idx <= BN and b[-idx] == '1':
                rnd += 1
            res = str(rnd % 2) + res
            rnd //= 2

        if rnd == 1:
            res = '1' + res

        return res