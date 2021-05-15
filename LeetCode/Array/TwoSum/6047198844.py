class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        left, right = 0, len(sorted_nums) - 1

        while left < right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum == target:
                return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]
            elif sum < target:
                left += 1
            else:
                right -= 1