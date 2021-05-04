import urllib.request
from functools import lru_cache


@lru_cache(None)
def is_palindromic(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindromic(s[1:len(s) - 1])


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for substr_len in range(1, len(s) + 1):
            for idx in range(0, len(s) - substr_len + 1):
                if is_palindromic(s[idx:idx + substr_len]):
                    res += 1
        return res