class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while 1:
            m = 0
            if len(s) == 1:
                return int(s) #한 자리 수이면 문자를 숫자로 리턴
            for i in s:
                m += int(i)

            s = str(m) #숫자를 문자로 만들어서 while문에서 다시 길이 검사 할 수 있게 함