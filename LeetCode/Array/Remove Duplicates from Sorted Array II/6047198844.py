class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        #nums를 스택으로 쓰자. i는 top을 가리킨다.
        for num in nums:
            if i < 2 or nums[i-2] != num:
                nums[i] = num
                i += 1
        return i