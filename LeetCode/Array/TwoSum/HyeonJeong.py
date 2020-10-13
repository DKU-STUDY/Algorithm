# 이중 for문
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j, n in enumerate(nums):
            for i, m in enumerate(nums[j+1:]):
                if n+m == target:
                    return [j, i+j+1]

# while문
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        j = 0
        i = 1
        while 1:
            if nums[j] + nums[i] == target:
                return [j, i]
            i += 1
            if i == length:
                j += 1
                i = j+1

# twoSum([2,7,11,15],9) == [0,1]
# twoSum([3,2,4],6) == [1,2]
# twoSum([3,3],6) == [0,1]
