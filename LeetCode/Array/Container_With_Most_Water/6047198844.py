class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin = 0
        end = len(height) - 1
        res = 0
        
        while begin < end:
            res = max(res,(end-begin)*min(height[begin],height[end]))
            if height[begin] < height[end]:
                begin+=1
            else:
                end-=1
        
        return res