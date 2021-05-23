class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_table = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        res = [] #틀림
        N = len(digits) 
        if N == 0:
            return res
        
        res.append("")
        
        #digit를 모든 res에 붙인다.
        for digit in digits:
            res_n = len(res)
            for _ in range(res_n):
                tmp = res.pop(0)
                for alpha in phone_table[digit]:
                    res.append(tmp+alpha)
        
        return res