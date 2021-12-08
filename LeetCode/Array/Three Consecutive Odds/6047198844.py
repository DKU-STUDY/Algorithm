class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for x in arr:
            # odd
            if x % 2 == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False