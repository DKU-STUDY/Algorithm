class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits)-1
        while i >= 0:
            if digits[i] == 10:
                if i == 0: # 가장 앞의 인덱스가 10이 되는 경우 숫자 분리
                    digits.insert(0, 1)
                    digits[i+1] = 0
                else:
                    digits[i-1] += 1
                    digits[i] = 0
            i -= 1
