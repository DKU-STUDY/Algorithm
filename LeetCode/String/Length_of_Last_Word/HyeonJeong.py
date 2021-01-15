class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = list(s.rstrip())
        slist.reverse()
        answer = 0
        for c in slist:
            if c != ' ':
                answer += 1
            else:
                return answer
        return answer
