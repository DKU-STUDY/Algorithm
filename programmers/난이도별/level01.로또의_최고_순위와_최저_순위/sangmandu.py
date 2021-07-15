'''
https://programmers.co.kr/learn/courses/30/lessons/77484
로또의 최고 순위와 최저 순위
[풀이]
'''
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    unk = lottos.count(0)
    win = 6 - len(set(win_nums) - set(lottos))
    return [rank[win + unk], rank[win]]
'''
'''