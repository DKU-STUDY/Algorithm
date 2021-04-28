class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1] # piles는 현재 presum으로 변경되었다.
        from functools import lru_cache # memoization에 사용.
        @lru_cache(None) # 크기 제한이 없음.
        def dp(p, m):
            if p + 2 * m >= N: return piles[p] # p는 현재 인덱스이고. 2*m 만큼 더할수있다.
            return piles[p] - min(dp(p + x, max(m,x)) for x in range(1, 2 * m +1))
        return dp(0,1)