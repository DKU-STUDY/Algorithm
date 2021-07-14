'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12913#
문제 : 땅따먹기
처음에는 index가 같을 때 (직전 반복에서의 두번째로 큰수+지금의 제일 큰수),
(직전 반복에서의 제일 큰수+지금의 두번째로 큰 수)를 구해서 비교해서
answer에 바로바로 더하고 수정하는 방식으로 풀이하였습니다.
그러니까 풀이도 너무 복잡해지고 다 틀렸다고 나와서 다른 사람들 질문을 보고
동적 프로그래밍을 사용해야 하는 문제임을 알았습니다.
index가 같을 때는 직전에서 두번째로 큰 값을,
index가 다를 때는 직전에서 제일 큰 값을 land에 바로 더하여 문제를 해결하였습니다.
다른 사람들 풀이를 보니 index를 비교하지도 않고,
max값과 두번째로 큰 값을 구하지도 않는 대단한 풀이가 있더라구요! ★ ω ★
[메모]
land[i][j] = max(land[i-1][:j]+land[i-1][j+1:]) + land[i][j]
'''

def solution(land):
    first, second = max(land[0]), sorted(land[0])[-2]
    index = land[0].index(first)

    for i in range(1, len(land)) :
        for j in range(4) :
            if index==j :
                land[i][j] += second
            else :
                land[i][j] += first
        first, second = max(land[i]), sorted(land[i])[-2]
        index = land[i].index(first)

    return max(land[-1])
