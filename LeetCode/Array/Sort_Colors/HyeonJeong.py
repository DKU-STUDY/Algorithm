class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for m in nums:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
