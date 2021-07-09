'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12949#
문제 : 행렬의 곱셈
처음에 [[0]*len(arr2[0])]*len(arr1)으로 했다가 답이 도저히 안나와서 엄청 헤맸다.
2차원배열 초기화 과정을 몰랐다.. 알고나니 너무 바보같다 ಥ︿ಥ
다른 사람 코드를 보니 arr2 앞에 *을 붙여 unpacking 하면 쉽게 행과 열을 바꿀 수 있더라구요
[메모메모]
[[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]
'''

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            for k in range(len(arr2)) :
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
