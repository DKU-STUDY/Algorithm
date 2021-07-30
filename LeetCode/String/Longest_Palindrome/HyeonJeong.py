class Solution:
    def longestPalindrome(self, s: str) -> int:
        alpha = list(set(list(s))) # 사용되는 알파벳 종류
        if len(alpha) == 1:
            return len(s)
        num = 0
        odd = 0
        for n in alpha:
            cnt = s.count(n)
            if cnt%2 == 0:
                num += cnt
            else:
                num += cnt-1 # 홀수도 최대한 많은 알파벳 이용
                odd = 1
        return num + odd