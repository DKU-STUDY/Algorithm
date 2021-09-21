class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #s를 dict에 등록하자
        dict1 = {}
        dict2 = {}
        idx = 0
        for char in zip(s,t):
            c1, c2 = char
            if c1 not in dict1:
                dict1[c1] = c2
            elif dict1[c1] != c2:
                return False
            if c2 not in dict2:
                dict2[c2] = c1
            elif dict2[c2] != c1:
                return False
        return True