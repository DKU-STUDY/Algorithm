class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: # 주어진 수가 음수일 경우
            answer = '-' + str(x)[-1:0:-1]
        else:
            answer = str(x)[-1::-1]
        answer = int(answer) # 가장 앞에 오는 숫자가 0인 경우
        if -2**31 <= answer <= 2**31 - 1: #해당 범위의 수 이상인 경우
            return answer
        return 0
