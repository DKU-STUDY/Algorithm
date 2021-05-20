class Solution:
# 짝수의 개수 찾는 문제
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if len(str(n))%2 == 0])
