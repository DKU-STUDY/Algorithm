class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [1] * n
        for cur in range(1,n):
            for past in range(cur):
                if nums[past] < nums[cur] and sub[past] + 1 > sub[cur]:
                    sub[cur] = sub[past] + 1
        return max(sub)