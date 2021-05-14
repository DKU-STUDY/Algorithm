class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #짝수개의 n
        nums.sort()
        return sum(i for i in nums[::2])