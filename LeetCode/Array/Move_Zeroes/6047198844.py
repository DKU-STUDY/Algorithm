class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = nums.count(0)

        for _ in range(N):
            nums.remove(0)
            nums.append(0)