'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12977
문제 : 소수 만들기
3개의 조합을 만드느라 애쓰다가 결국 검색 찬스로 itertools라는 것을 알게 됐습니다.
저번주 은행 코테에서 itertools를 알고 있었으면 풀 수 있었을 문제가 있던터라 너무나 아쉽...〒▽〒
저는 prime 변수를 추가로 이용해서 break 했는지 확인하였는데
for else문을 사용하면 별도의 변수 지정 없이 바로 확인이 가능하더라구요!!!
'''

from itertools import combinations

def solution(nums):
    answer = 0
    com = list(combinations(nums,3))
    for i in com :
        prime = True
        s = sum(i)
        for j in range(2,s//2+1) :
            if s%j == 0 :
                prime = False
                break
        if prime : answer += 1
    return answer
