class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []
        answer = []
        s = ""
        slist = []
        for c in digits:
            if int(c) < 7:
                for i in range(3):
                    s += chr(97+ i+ 3*(int(c)-2))
            elif c == '7':
                for n in 'pqrs':
                    s += n
            elif c == '8':
                for n in 'tuv':
                    s += n
            elif c == '9':
                for n in 'wxyz':
                    s += n
            slist += [s]
            s = ""
        for c1 in slist[0]:
            if length == 1:
                answer += [c1]
            else:
                for c2 in slist[1]:
                    if length == 2:
                        answer += [c1+c2]
                    else:
                        for c3 in slist[2]:
                            if length == 3:
                                answer += [c1+c2+c3]
                            else:
                                for c4 in slist[3]:
                                    answer += [c1+c2+c3+c4]
        return answer