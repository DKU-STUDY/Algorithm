class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left를 구한다.
        left = [1]
        for i in range(len(nums)-1):
            left.append(left[-1]*nums[i])
        
        right = [1]
        for i in range(len(nums)-1,0,-1):
            right.append(right[-1]*nums[i])

        return [t[0]*t[1] for t in zip(left,right[::-1])]