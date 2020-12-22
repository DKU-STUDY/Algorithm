class Solution:
    def arrangeWords(self, text: str) -> str:
        slist = text.split(' ')
        slist[0] = slist[0][0].lower() + slist[0][1:] # 문장의 첫번째 글자를 소문자로 바꿈
        slist.sort(key = lambda s: len(s))
        slist[0] = slist[0][0].upper() + slist[0][1:] # 문장의 첫번째 글자를 대문자로 바꿈
        return ' '.join(slist)