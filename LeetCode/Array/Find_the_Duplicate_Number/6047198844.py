class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i])>1 :
                return nums[i]
    
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n2)?
        