class Solution:
    def maximumSwap(self, num: int) -> int:
    # 정수의 두자리를 최대 1번 바꿔서 최대의 수를 만드는 방법
    # 0번 : 이미 수가 최대
    # 1번 : 가장 높은 자리 수부터 최대 정수와 비교했을 때, <처음으로 발견된 다른 자리인 수>와 <다른 자리 보다 아래 자리인 수 중 최대값(최대값이 2개 이상일때는 가장 낮은 자리 수)>의 자리를 바꾼 수
        n = [int(x) for x in str(num)]
        sort_n = sorted(n, reverse = True)
        length = len(n)

        if sort_n == n:
            return num
        else:
            for i, m in enumerate(n):
                if m != sort_n[i]:
                    tmp = n[i]
                    n[i] = n[length-(n[-1::-1].index(max(n[i+1:]))+1)]
                    # length-(n[-1::-1].index(max(n[i+1:]))+1)
                    # : n 리스트의 현재 인덱스(i)의 뒤 리스트([i+1:])에서 최대값을 찾고, n 리스트의 뒤에서부터 최대값을 찾아서 가장 먼저 발견되는 인덱스
                    n[length-(n[-1::-1].index(max(n[i+1:]))+1)] = tmp
                    break

        s = ""
        for c in n:
            s += str(c)
        return int(s)
