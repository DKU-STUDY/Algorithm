'''
https://programmers.co.kr/learn/courses/30/lessons/68936
쿼드압축 후 개수 세기
특정 영역에 대해 자신과 자신의 위쪽과 자신의 왼쪽 그리고 자신의 왼쪽 위가 동일하다면 쿼드압축을 할 수 있다.
이 때 쿼드압축이 가능하다면 자신을 제외한 좌상 주변을 -1로 설정. 자신은 문자열 타입으로 변환한다.

8x8를 기준으로 설명하면,
	영역 2x2 검사 ( 1 1 ) ( 1 3 ) ( 1 5 ) ( 1 7 ) ( 3 1 ) ( 3 3 ) ( 3 5 ) ( 3 7 ) ( 5 1 ) ( 5 3 ) ( 5 5 ) ( 5 7 ) ( 7 1 ) ( 7 3 ) ( 7 5 ) ( 7 7 )
	영역 4x4 검사 ( 3 3 ) ( 3 7 ) ( 7 3 ) ( 7 7 )
	영역 8x8 검사 ( 7 7 )
다음과 같은 인덱스를 검사해야 한다.

4x4를 기준으로 예를 들면,
1 1 0 0    1  1  -1 -1
1 0 0 0    1  0  -1 '0'
1 0 0 1    1  0  0  1
1 1 1 1    1  1  1  1
(전)         (후)

이 후 압축이 불가능 하면
0과 '0'의 개수, 1과 '1'의 개수를 반환한다.
'''

import math
def solution(arr):
    size = len(arr)
    n = int(math.log2(size))
    for m in range(1, n+1):
        for i in range(2**m-1, size, 2**m):
            for j in range(2**m-1, size, 2**m):
                if arr[i-2**(m-1)][j-2**(m-1)] == arr[i-2**(m-1)][j] == arr[i][j-2**(m-1)] == arr[i][j]:
                    arr[i-2**(m-1)][j-2**(m-1)] = arr[i-2**(m-1)][j] = arr[i][j-2**(m-1)] = -1
                    arr[i][j] = str(arr[i][j])
    return [sum([i.count(0) + i.count('0') for i in arr]), sum(i.count(1) + i.count('1') for i in arr)]

'''
'''