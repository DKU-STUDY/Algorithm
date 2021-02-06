class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        j = 0
        i = 0
        while j < len(slist) and i < len(tlist):
            if slist[j] != tlist[i]:
                tlist.pop(i)
            else:
                i += 1
                j += 1
        print(slist)
        print(tlist)
        return True if slist == tlist[:len(slist)] else False
