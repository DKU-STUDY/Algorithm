class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        for i in range(1, len(nums)+1): # 더해져야하는 마지막 번째 수가 1 ~ len(nums)+1
            n = 0
            for j in range(0, i):
                n += nums[j]
            sum.append(n)
        return sum