class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if char in dict.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if stack.pop()!=dict[char]:
                    return False

        return not stack