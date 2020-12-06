class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        slist = []
        while 1:
            c_sum = 0
            for c in s:
                c_sum += int(c)*int(c)
            s = str(c_sum)
            if s in slist or s == '1': # 무한반복 중지
                break
            slist += [s]
        if s == '1':
            return True
        return False