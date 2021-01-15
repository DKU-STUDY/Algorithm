class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num = bin(N)
        answer = ''
        for i in num[2:]:
            if i == '0':
                answer += '1'
            else:
                answer += '0'
        return int(answer, 2) # 2진수를 10진수로