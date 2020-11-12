'''
https://programmers.co.kr/learn/courses/30/lessons/42586
기능 개발 : 우선순위 큐의 모든 원소들에 동일한 값이 더해질 때 조건부 팝
각 작업이 같은 날 팝 되면 같은 dict에서 카운트되도록 함'''


def solution(progresses, speeds):
    day = 1
    comp = {}
    for p, s in zip(progresses, speeds):
        while p + s * day < 100:
            day += 1
        comp.setdefault(day, 0)
        comp[day] += 1
    return list(map(lambda x: x[1], sorted(comp.items(), key=lambda x: x[0])))


'''
'''