import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        candidate = itertools.product([")","("],repeat=n)
        
        def is_valid(element):
            stack = []
            for parentheses in element:
                if parentheses == '(':
                    stack.append('(')
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            return True
        
        for j in itertools.product(candidate,repeat=2):
            k, l = j
            element = ''.join(k+l)
            if is_valid(element):
                answer.append(element)
        return answer