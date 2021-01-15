# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복을 lost한 친구가 index-1, index+1 친구에게만 빌릴 수 있는 문제
# 오름차순에서는 무조건 근처번호에게 빌리면 문제가 없음

def solution(n, lost, reserve):
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]

    for i in _reserve:
        if i - 1 in _lost:
            _lost.remove(i - 1)
        elif i + 1 in _lost:
            _lost.remove(i + 1)

    return n - len(_lost)