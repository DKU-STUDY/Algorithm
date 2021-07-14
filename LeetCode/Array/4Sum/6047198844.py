class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,N):
                if j != i+1 and nums[j-1] == nums[j]:
                    continue
                begin = j+1
                end = N-1
                
                while begin < end:
                    s = nums[i] + nums[j] + nums[begin] + nums[end]
                    if s == target:
                        answer.append([nums[i],nums[j],nums[begin],nums[end]])
                        while begin < N-1 and nums[begin] == nums[begin+1]:
                            begin += 1
                        while end > 0 and nums[end] == nums[end-1]:
                            end -= 1
                        begin += 1
                        end -= 1
                        
                    elif s < target:
                        begin += 1
                    else:
                        end -= 1
        return answer