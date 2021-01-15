class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = []
        for x in range(len(s)): #문자의 시작점 설정
            word = ""
            n = x
            while 1:
                if n < len(s) and s[n] not in word: #문자열에서 다른 문자인 경우는 누적
                    word += s[n]
                    n += 1
                else:
                    slist.append(len(word)) #이미 담긴 문자인 경우는 길이를 배열에 담고 while문 종료
                    break
        return 0 if slist == [] else max(slist)