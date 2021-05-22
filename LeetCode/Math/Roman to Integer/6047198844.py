'''
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_code = {"I":"1", "V":"5", "X":"10", "L":"50", "C":"100", "D":"500", "M":"1000"}
        s = list(s)
        s = [int(roman_code[i]) for i in s]
        
        result = 0
        
        print(s)
        
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i] < s[i+1]:
                result += s[i+1] - s[i]
                i += 2
            else:
                result += s[i]
                i += 1
                
        return result

#XLIX