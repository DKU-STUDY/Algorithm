class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
    # arr 배열에서 누락된 k번째 정수 반환하는 문제
        result = 0
        i = 0
        while (k != -1): # k번째 정수가 반환되기 위해서 k=0까지 돌아가야함
            if i not in arr:
                result = i
                k -= 1
            i += 1  # max(arr) <= 1000이므로 i <= 1001+k
        return result
