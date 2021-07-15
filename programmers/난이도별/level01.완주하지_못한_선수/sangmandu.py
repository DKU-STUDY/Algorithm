'''
https://programmers.co.kr/learn/courses/30/lessons/42576
완주하지 못한 선수
[풀이]
1. 정렬 후 비교
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, v in enumerate(completion):
        if v != participant[i]:
            return participant[i]
    return participant[-1]
'''
이 문제는 해시로 푸는 문제라서
dictionary로 푸는 방법이 성능이 더 빠름
'''