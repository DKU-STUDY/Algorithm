class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(idx):
            if idx == len(nums) - 1:
                return 0
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = 9999999
            for dx in range(1, nums[idx] + 1):
                if idx + dx < len(nums):
                    memo[idx] = min(memo[idx], 1 + dp(idx + dx))
            return memo[idx]

        return dp(0)