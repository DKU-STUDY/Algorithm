import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[-1][0]