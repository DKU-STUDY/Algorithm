class Solution:
    def convert(self, s: str, numRows: int) -> str:
        nlist = []
        alist = []
        for i in range(numRows):
            nlist += [i]
            alist += [[]]
        number = nlist + sorted(nlist, reverse=True)[1:-1]
        # numRows에 따라 인덱스 순서의 반복 구간이 number에 리스트로 담김

        n = 0
        i = 0
        while 1:
            alist[number[i]] += s[n] # 해당하는 리스트 위치에 주어진 s를 넣음
            n += 1
            i += 1
            if i == len(number): # 반복 구간을 반복될 수 있게 함
                i = 0
            if n == len(s): # s의 길이만큼 s의 문자들이 들어갈 수 있게 함
                break

        answer = []
        for s in alist:
                answer += s
                # 지그재그로 정리된 문자들이 answer에 담기게 됨

        return ''.join(answer)
