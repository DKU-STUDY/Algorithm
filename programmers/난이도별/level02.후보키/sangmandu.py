'''
https://programmers.co.kr/learn/courses/30/lessons/42890
후보키 : 유일성과 최소성을 만족하는 데이터 찾기
L2 에서 제일 어려운 문제라고 생각한다. https://eda-ai-lab.tistory.com/505 참고
'''

from itertools import combinations

def solution(relation):
    col, row = len(relation), len(relation[0])
    cases = [j for i in range(1, row + 1) for j in combinations(range(row), i)]

    unique = []
    for case in cases:
        tmp = [tuple(r[num] for num in case) for r in relation]
        if len(set(tmp)) == col: unique.append(case)

    minimality = set(unique[:])
    for i in range(len(unique) - 1):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(unique[j])):
                minimality.discard(unique[j])

    return len(minimality)


'''
'''