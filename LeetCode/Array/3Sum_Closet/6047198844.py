class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        dif = 10**3 + 1 
        res = 0
        
        for i in range(len(nums)):
            #nums[i]는 무조건 더한다.
            #목표는 t를 만드는것.
            t = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                s = nums[left] + nums[right]
                if dif > abs(t-s):
                    dif = abs(t-s)
                    res = s + nums[i]
                
                #s가 target에 가깝게 조정되어야한다.
                if s > t:
                    right -= 1
                elif s <= t:
                    left += 1
        return res