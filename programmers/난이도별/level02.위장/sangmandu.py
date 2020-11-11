'''
https://programmers.co.kr/learn/courses/30/lessons/42578
위장 : 해시 문제
dictionary에 의상 별 갯수를 저장해서 조합할 수 있는 경우의 수 계산
'''

def solution(clothes):
    otjang = {}    #https://www.youtube.com/watch?v=Hfp77VwW950
    for _, a in clothes:
        otjang.setdefault(a, 0)
        otjang[a] += 1
    answer = 1
    for i in otjang.values():
        answer *= (i+1)
    return answer-1


'''
answer 라는 새로운 메모리 사용대신 reduce를 사용할 수 있다.
dictionary값이 개수라면 counter 사용
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
'''