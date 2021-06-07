'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12944
문제 : 평균 구하기
하샤드 수 문제를 풀 때 한 줄의 코드로 덧셈을 하는 것을 보고 이를 따라해봤습니다.
그런데 여기서는 list라 훨씬 쉽게 하는 방법이 있어 메모합니다.
[메모메모]
sum(arr) / len(arr)
'''

def solution(arr):
    answer = sum([x for x in arr]) / len(arr)
    return answer
