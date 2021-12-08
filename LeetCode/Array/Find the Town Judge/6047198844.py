class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        # 모든 주민이 믿는다.
        # B의개수 == n-1 == judge
        # A의개수 == 0
        A = Counter([a for a, b in trust])
        B = Counter([b for a, b in trust]).items()
        for b, b_count in B:
            if b_count == n-1 and A[b] == 0:
                return b
        return -1