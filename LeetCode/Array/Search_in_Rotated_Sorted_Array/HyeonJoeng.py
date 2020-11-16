class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        answer = [i for i, x in enumerate(nums) if x == target]
        return int(answer[0])
