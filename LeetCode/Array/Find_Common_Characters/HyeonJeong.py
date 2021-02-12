class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        s = []
        for a in A:
            s += [list(a)]

        result = []
        for j in range(len(s[0])):
            for i in range(1, len(s)):
                if s[0][j] not in s[i]:
                    break
                if i == len(s)-1:
                    result += s[0][j]
                    for x in range(1, len(s)):
                        s[x].remove(s[0][j])
        return result
