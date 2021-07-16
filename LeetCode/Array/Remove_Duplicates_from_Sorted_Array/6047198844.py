class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #삽입 idx
        idx = 0
        
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        
        for _ in range(idx,len(nums)):
            nums.pop()