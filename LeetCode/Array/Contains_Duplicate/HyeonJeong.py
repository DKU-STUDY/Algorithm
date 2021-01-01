class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nlist = sorted(nums)
        length = len(nlist)
        for i in range(length-1):
            if nlist[i] == nlist[i+1]:
                return True
        return False
