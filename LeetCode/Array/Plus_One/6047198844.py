class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[-1] += 1
        N = len(digits) - 1
        
        for i in range(N,-1,-1):
            digits[i-1] += digits[i] // 10
            digits[i] %= 10
        
        if digits[0] == 0:
            digits.pop(0)
        
        return digits