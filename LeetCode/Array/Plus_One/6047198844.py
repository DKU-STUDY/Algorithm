class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        return digits