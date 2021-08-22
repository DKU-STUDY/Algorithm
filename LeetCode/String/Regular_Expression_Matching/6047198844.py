class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        memo = [[None for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        def matching(s, p) -> bool:
            m = len(s)
            n = len(p)

            if memo[m][n] != None:
                return memo[m][n]

            if not s:
                if not p:
                    memo[m][n] = True
                    return memo[m][n]
                elif len(p) > 1 and p[1] == '*':  # *를 무시한다.
                    memo[m][n] = matching(s, p[2:])
                    return memo[m][n]
                else:  # p를 줄일수없다.
                    memo[m][n] = False
                    return memo[m][n]
            elif not p:  # s는 있는데 p가 없으면 False
                memo[m][n] = False
                return memo[m][n]

            if p[0] == '.' or s[0] == p[0]:  # 앞자리가 같은 경우
                if len(p) > 1 and p[1] == '*':  # *를 한번 더 쓰는 경우. *를 쓰는 경우, *를 무시하는 경우
                    memo[m][n] = matching(s[1:], p) or matching(s[1:], p[2:]) or matching(s, p[2:])
                    return memo[m][n]
                else:  # 이외의 경우는 무시할수없다.
                    memo[m][n] = matching(s[1:], p[1:])
                    return memo[m][n]
            elif len(p) > 1 and p[1] == '*':  # 같지 않은 경우. *를 무시할수있다.
                memo[m][n] = matching(s, p[2:])
                return memo[m][n]
            else:  # 방법이없다.
                memo[m][n] = 0
                return memo[m][n]

        return matching(s, p)