#lstrip
#삼항연산자
#정규표현식
#join
#findall함수

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s = re.findall('^[+\-]?\d+', s)
        
        print(s)
        print(''.join(s))
        
        try:
            res = int(''.join(s))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN: 
                return MIN
            return res
        except: 
            return 0
        

        