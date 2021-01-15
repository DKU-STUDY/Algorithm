class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [nums.index(target), len(nums)-nums[-1::-1].index(target)-1]
