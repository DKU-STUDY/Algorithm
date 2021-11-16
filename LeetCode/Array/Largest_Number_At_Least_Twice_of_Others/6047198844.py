class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_number = max(nums)
        cnt = 0
        for num in nums:
            if num != largest_number and num * 2 > largest_number:
                return -1
        return nums.index(largest_number)