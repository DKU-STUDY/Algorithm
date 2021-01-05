'''
https://leetcode.com/problems/divisor-game/
기본적인 dp 문제(인줄 알았다)
'''

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N+1)
        for num in range(2, N+1):
            divisor = [1]
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    divisor.append(i)
                    divisor.append(num // i)
            dp[num] = True if False in [dp[num-d] for d in divisor] else False
        return dp[N]


'''
아니 겁나 열심히 풀었는데 짝홀수 구별 문제라니
아마 숨겨진 전제조건이 있다면 alice와 bob은
이기기 위한 최선의 결정을 한다는 점.
'''