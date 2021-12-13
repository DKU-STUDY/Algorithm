class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += len(str(num)) % 2 == 0
        return res