class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):# 중복되는 값을 지우다가 없는 인덱스에 접근하지 않게 종료
            if nums[i] == nums[i+1]: # 중복되는 값 확인
                del nums[i+1] # 해당 인덱스 위치의 값을 제거
                i -= 1 # 다음 값들의 인덱스가 -1 됨
            i += 1
        return len(nums)