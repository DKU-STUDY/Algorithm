class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        length = len(s)
        while i < length:
            if i+1 < length and d[s[i]] < d[s[i+1]]:
                    answer += d[s[i+1]]- d[s[i]]
                    i += 2
            else:
                answer += d[s[i]]
                i += 1
        return answer