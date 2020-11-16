'''
https://programmers.co.kr/learn/courses/30/lessons/42889
실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
실패율을 오름차순과 내림차순이 섞여있는 기준으로 정렬 하기
key = (x[0], -x[1])을 사용하면 섞여있는 정렬 가능.
'''

def solution(N, stages):
    failure = [stages.count(i) for i in range(1, N+2)]
    play = [sum(failure[i:]) for i in range(N)]
    rate = [(i, v[0]/v[1]) if v[1] != 0 else (i, v[0] and 1) for i, v in enumerate([a, b] for a, b in zip(failure, play))]
    return list(map(lambda x : x[0]+1, sorted(rate, key=lambda x: (x[1], -x[0]), reverse=True)))

'''
'''