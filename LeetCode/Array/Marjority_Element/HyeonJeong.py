class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        s = list(set(nums)) # set으로 중복제거
        for n in s:
            if nums.count(n) > length/2: # count()로 해당개수 찾아서 비교
                return n