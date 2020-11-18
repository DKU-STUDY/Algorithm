class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        # int(문자열, 2) : 문자열을 읽어서 2진수로 바꿈
        # sum에는 두 숫자가 합쳐진 10진수가 저장됨
        return bin(sum)[2:]
        # bin()이 해당 숫자를 이진수로 만들고 문자열로 반환시킴
