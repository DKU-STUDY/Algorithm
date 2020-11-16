# https://www.acmicpc.net/problem/18870

"""
시간 제한	    메모리 제한	제출	    정답	    맞은 사람	    정답 비율
2 초	    512 MB	    1772	1072	758	        62.387%

문제
    수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
    Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
    X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
    첫째 줄에 N이 주어진다.
    둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
    첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
    1 ≤ N ≤ 1,000,000
    -109 ≤ Xi ≤ 109
"""

# 사실 아직 잘 모르겠다. 좌표압축이라는 개념이 이런게 아닌거같은데?

from sys import stdin


N = int(stdin.readline())

coo_list = list(map(int, stdin.readline().split()))

temp = []
dic = {}

for coordinate in coo_list:
    if coordinate not in dic:
        dic[coordinate] = 0
        temp.append(coordinate)

temp.sort()

for idx in range(len(temp)):
    dic[temp[idx]] = idx

return_str = ''

for idx in range(len(coo_list)):
    return_str += str(dic[coo_list[idx]]) + ' '

print(return_str[:-1])
