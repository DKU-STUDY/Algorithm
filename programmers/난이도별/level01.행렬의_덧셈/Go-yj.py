'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12950
문제 : 행렬의 덧셈
중첩 for문을 이용하여 리스트 원소 값을 하나하나 더하였습니다.
다른 사람 풀이에 numpy를 이용하여 간단하게 더하는 탐나는 방법이 있어 메모
[메모메모]
import numpy as np
A = np.array(arr1)
B = np.array(arr2)
answer = A+B
return answer.tolist()
'''

def solution(arr1, arr2):
    answer = [[] for x in range(len(arr1))]
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer
