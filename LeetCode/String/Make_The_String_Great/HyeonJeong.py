class Solution:
    def makeGood(self, s: str) -> str:
        result = [c for c in s]
        i = 0
        while i < len(result)-1:
            if ord(result[i])-32 ==  ord(result[i+1]) or ord(result[i]) ==  ord(result[i+1])-32:
            # 연속된 인덱스에 같은 알파벳의 대문자와 소문자인 경우
                result.pop(i+1)
                result.pop(i)
                if i != 0:
                    i -= 1
            else:
                i += 1
        return "".join(result)
