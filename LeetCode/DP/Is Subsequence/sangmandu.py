'''
https://leetcode.com/problems/is-subsequence
인덱스 순서 비교
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for word in t:
            if i == len(s):
                return True
            if s[i] == word:
                i += 1
        return i == len(s)

'''
'''