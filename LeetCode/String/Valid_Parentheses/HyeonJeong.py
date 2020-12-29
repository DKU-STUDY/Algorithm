class Solution:
    def isValid(self, s: str) -> bool:
        slist = []
        for i, c in enumerate(s):
            if c in '({[':
                slist.append(c)
            else:
                if len(slist) < 1:
                    return False
                elif ')' == c and '(' == slist[-1]:
                    slist.pop()
                elif ']' == c and '[' == slist[-1]:
                    slist.pop()
                elif '}' == c and '{' == slist[-1]:
                    slist.pop()
                else:
                    return False
        if slist == []:
            return True
        return False