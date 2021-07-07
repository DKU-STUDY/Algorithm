'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/77484
문제 : 로또의 최고 순위와 최저 순위
lottos의 숫자가 win_nums에 있는지 확인하고,
0이 모두 정답일 때와 0이 모두 정답이 아닐 때를 넣어줍니다.
'''

def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    win = 0
    zero = lottos.count(0)
    for i in set(lottos) :
        if i in win_nums :
            win += 1
    answer.append(rank[win+zero])
    answer.append(rank[win])
    return answer
