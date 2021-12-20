class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in gain:
            res.append(res[-1] + i)
        return max(res)