'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12982
문제 : 예산
오름차순으로 정렬하여 작은 수부터 더해 예산을 넘는지 확인해주었습니다.
'''

def solution(d, budget):
    answer = 0
    n = 0
    if sum(d) <= budget : return len(d)
    for i in sorted(d) :
        if n+i <= budget :
            n += i
            answer += 1
    return answer
