'''
https://programmers.co.kr/learn/courses/30/lessons/12913
땅따먹기
[풀이]
1. max 값을 아래 리스트로 내려보낸다. 바로 아래는 두번째 max값을 전달.
'''
def solution(land):
    one = two = idx = 0
    for i in land:
        for j in range(4):
            i[j] += one
        i[idx] += two - one
        idx = i.index(max(i))
        one, two = sorted(i)[-1], sorted(i)[-2]

    return max(land[-1])
print(
    solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
)

'''
이렇게 풀고 싶었던 것이 맞다.
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
'''