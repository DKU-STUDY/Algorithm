'''
https://programmers.co.kr/learn/courses/30/lessons/42840#
모의고사
[풀이]
0. 각자의 비법을 실제 문제와 비교 True 개수를 비교하여 출력
'''
def solution(answers):
    size = len(answers)
    score = lambda x, y : x == y
    one = list(map(score, answers, [1,2,3,4,5]*(size // 5 + 1))).count(True)
    two = list(map(score, answers, [2,1,2,3,2,4,2,5]*(size // 8+ 1))).count(True)
    thr = list(map(score, answers, [3,3,1,1,2,2,4,4,5,5]*(size // 10 + 1))).count(True)
    answers = [one, two, thr]
    return [i+1 for i in range(3) if answers[i] == max(one, two, thr)]
'''
'''