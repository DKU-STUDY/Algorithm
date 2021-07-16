class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
            5000: ""
            }
        
        ans = ""
        for div in (1000, 100, 10, 1):
            converted = num // div
            if converted*div in table:
                ans += table[converted*div]
            else:
                five, one = converted//5, converted%5
                ans += table[5*div]*five
                ans += table[div]*one
            num %= div
        
        return ans
            