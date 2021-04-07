class Solution:
# 리스트에 숫자가 1번만 나오는 경우를 반환하는 문제
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if n not in result:
                result.append(n)
            else: # 반복된 수는 결과 리스트에서 제거
                result.remove(n)
        return result
