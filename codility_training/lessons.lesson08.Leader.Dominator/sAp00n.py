# N 개의 정수로 구성된 배열 A가 제공됩니다. 배열 A 의 지배자 는 A 요소의 절반 이상에서 발생하는 값입니다.
# N은 [ 0 .. 100,000 ] 범위 내의 정수 이며
# 배열 A의 각 요소는 [ -2,147,483,648 .. 2,147,483,647 ] 범위 내의 정수 이다.

def solution(A):
    # write your code in Python 3.6
    len_a = len(A)
    condition = len_a // 2
    dic = {}
    for i in A:
        if i in dic:
            dic[i] = dic.get(i, 0) +1
            if dic[i] > condition:
                return A.index(i)
    if len(list(dic.keys())) == 1:
        return 0
    else:
        return -1
