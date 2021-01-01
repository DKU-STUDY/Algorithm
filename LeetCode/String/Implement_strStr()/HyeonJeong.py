class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1
