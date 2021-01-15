class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1): # for문은 O(n), len()은 O(1) 시간복잡도를 가짐
            if i not in nums:
                return i
