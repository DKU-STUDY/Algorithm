class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while 1:
            if len(s) == 1:
                return int(s) #한 자리 수이면 문자를 숫자로 리턴
            s = str(sum([int(i) for i in s]))
           #숫자를 문자로 만들어서 while문에서 다시 길이 검사 할 수 있게 함