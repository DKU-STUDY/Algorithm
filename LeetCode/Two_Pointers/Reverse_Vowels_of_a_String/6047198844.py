class Solution:
    def reverseVowels(self, s: str) -> str:
        word = ''
        N = len(s)
        begin, end = 0, N - 1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])

        while begin < N:
            if s[begin] in vowels:
                while s[end] not in vowels:
                    end -= 1
                word += s[end]
                end -= 1
            else:
                word += s[begin]
            begin += 1

        return word