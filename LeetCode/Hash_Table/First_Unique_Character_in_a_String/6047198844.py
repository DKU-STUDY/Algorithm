class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = Counter(s)
        for idx, char in enumerate(s):
            if table[char] == 1:
                return idx
        return -1