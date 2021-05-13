import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9A-Z]','',s).lower()
        return s == s[::-1]