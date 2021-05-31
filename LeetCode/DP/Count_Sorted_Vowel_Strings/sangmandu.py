'''
https://leetcode.com/problems/count-sorted-vowel-strings/
Count Sorted Vowel Strings
DP 문제인데 DP로 풀지못한..
'''
class Solution(object):
    def countVowelStrings(self, n):
        vowel = [1, 1, 1, 1, 1]
        while n != 1:
            n -= 1
            temp = vowel[:]
            for idx in range(5):
                for idx2 in range(idx+1, 5):
                    vowel[idx2] += temp[idx]
        return sum(vowel)

'''
2차원 행렬 선언해서 DP쪽으로 풀고싶었는데, 잘 생각이 안났다.
세부적인 원리는 비슷한 것 같다.
왜냐하면 a가 eiou로, e가 iou로, ... 하나씩 추가해주는 메커니즘이
DP 방식이랑 동일하기 때문

아래 코드는 DP로 구현한 코드.
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = [[ 0 for col in range(6)] for row in range(n + 1)]
        
        for str_len in range(1, n + 1):
            for vowel_len in range(1, 6):
                if str_len == 1:
                    dp[str_len][vowel_len] = dp[str_len][vowel_len - 1] + 1
                else:
                    dp[str_len][vowel_len] = dp[str_len - 1][vowel_len] + dp[str_len][vowel_len - 1]
        
        return dp[n][5]
'''