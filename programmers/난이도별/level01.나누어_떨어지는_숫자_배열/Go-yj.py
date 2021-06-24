'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12910
문제 : 나누어 떨어지는 숫자 배열
나머지 확인하고 추가하는 과정을 그냥 정석대로 나타냄
다른 사람 코드 보니 for문과 if 문을 한 줄로 써버리던데
한 줄로 쓰는 것은 의식하고 연습하지 않으면 놓치기 쉽고 익숙해지지 않는 것 같다
앞으로 코드 써보고 간단하게 줄여보는 연습도 함께 꼭 해봐야겠다
[메모]
sorted([i for i in arr if i%divisor==0])
'''

def solution(arr, divisor):
    answer = []
    for i in arr :
        if i%divisor==0 : answer.append(i)
    if not answer : answer.append(-1)
    return sorted(answer)
