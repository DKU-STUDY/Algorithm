from math import factorial

class Solution:
    def trailingZeroes(self, n: int) -> int:
    # n!의 결과에서 후행 0의 개수 구하는 문제
        if n == 0: return 0
        result = list(str(factorial(n)))
        # n!의 결과의 길이와 각 자리수를 분리해서 보기 위해 list 처리
        index = len(result) - 1
        cnt = 0
        while (index >= 0):
            if result[index] != '0':
                break
            else:
                index -= 1
                cnt += 1
        return cnt
