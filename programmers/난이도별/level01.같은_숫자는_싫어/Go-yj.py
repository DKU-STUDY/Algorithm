'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12906
문제 : 같은 숫자는 싫어
빈 값일 때 arr[-1]을 하면 런타임 에러가 발생해서
if elif로 비었을 때를 미리 처리해주었는데
arr[-1:]을 사용하면 빈 값이어도 죽지 않는다네요 (✪ ω ✪)
[메모]
if answer[-1:] != arr[-1] : answer.append(arr[-1])
'''

def solution(arr):
    answer = [arr[i] for i in range(len(arr)-1) if arr[i] != arr[i+1]]
    if not answer : answer.append(arr[-1])
    elif answer[-1] != arr[-1] : answer.append(arr[-1])
    return answer
