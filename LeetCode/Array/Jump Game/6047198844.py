sys.setrecursionlimit(10 ** 8)


def jump(cur, dst, nums, memo) -> bool:
    if cur >= dst:
        return True
    if memo[cur] != -1:
        return memo[cur]

    memo[cur] = 0
    for step in range(nums[cur], 0, -1):
        if jump(cur + step, dst, nums, memo):
            memo[cur] = 1
            break

    return memo[cur]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        return jump(0, len(nums) - 1, nums, memo)