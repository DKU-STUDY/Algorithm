'''
https://leetcode.com/problems/maximum-subarray/
DP : max값을 기록하면서, cur값을 갱신해가기
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        for num in nums[1:]:
            curSum=max(num, curSum+num)
            maxSum=max(curSum, maxSum)
        return maxSum

'''
'''