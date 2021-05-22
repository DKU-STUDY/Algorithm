class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:  # left와 right를 가지고 투포인터 연산을 수행.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 예외처리: 아래 알고리즘은 길이가 1일때 처리를 하지 못한다.
        # 인덱스 슬라이싱이 빠르므로 인덱스 슬라이싱을 이용한다.
        if len(s) < 2 or s[:] == s[::-1]:
            return s

        # i가 최대 len(s)-2까지 증가할수있다.
        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result