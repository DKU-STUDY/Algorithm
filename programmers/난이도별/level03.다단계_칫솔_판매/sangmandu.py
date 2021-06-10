'''
https://programmers.co.kr/learn/courses/30/lessons/77486
다단계 칫솔 판매
[풀이]
1. 딕셔너리 선언 : 판매자 : [추천인, 자신의 수익]
2. 자신이 벌어든 이익을 profit = 100 * amount 로 정의
3. 자신의 추천인이 없거나, 더이상 10%로 나눠지지 않을 때 까지 수익 분배
4. 더 이상 10%로 나눠지지 않을 때는 해당 금액을 마지막 사람이 얻는 조건을 추가
5. enroll 순서에 맞게끔 각자의 수익 반환
'''
import math
def solution(enroll, referral, seller, amount):
    dic = {e: [r, 0] for e, r in zip(enroll, referral)}
    for s, a in zip(seller, amount):
        profit = 100 * a
        while s != '-' and int(profit * 0.1) != 0:
            mine, profit = math.ceil(profit * 0.9), math.floor(profit * 0.1)
            dic[s][1] += mine
            s = dic[s][0]
        if s != '-':
            dic[s][1] += profit

    return [dic[e][1] for e in enroll]
'''
'''