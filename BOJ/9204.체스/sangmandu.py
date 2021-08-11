'''
https://www.acmicpc.net/problem/9204
체스
[풀이]
1. 열 좌표가 문자이므로, 행 좌표와 동일하게 설정한다
=> A는 1, ... , H는 8
=> 이 때 ord()를 사용한다. ord(A) = 65
=> 추후에, 알파벳 좌표로 변환할 때는 chr() 사용
2. 시작좌표와 도착좌표에서 움직일 수 있는 대각선 좌표들을 모두 구한다.
=> 이들을 각각 diagonal[0]과 diagonal[1]에 할당
=> 체스판의 끝지점에 도달할 때 까지 대각선방향으로 이동할 수 있는 좌표를 모두 구한다
=> 이러한 과정을 총 4방향으로 진행한다.
=> 도달할 수 있는 좌표들은 튜플 형태로 각각의 대각선 리스트에 추가한다.
=> 추후에, set형태로 비교할 것이기 때문에 리스트가 아닌 튜플 형태로 추가한다.
3. 비교하는 방법은 다음과 같다.
3-1. 두 점이 같을 경우
=> print(0, x1, y1)
3-2. 시작좌표의 대각선 이동범위 안에 도착 좌표가 있을 경우
=> print(1, x1, y1, x2, y2)
3-3. 시작좌표의 대각선 이동범위와 도착좌표의 대각선 이동범위안에 둘 다 속하는 좌표가 존재할 경우
=> 이 좌표를 x3, y3 라 하자
=> print(2, x1, y1, x3, y3, x2, y2)
=> 이 때 diagonal을 set형태로 만들고 intersect()를 이용해 교집합을 구한다.
3-4. 이 외에는 방법이 없다
=> print("Impossible")
=> 이 방법은 시작좌표의 합과 도착좌표의 합이 각각 홀수나 짝수로 동일한지 여부로 구할 수도 있다
'''
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = input().split()
    if x1 == x2 and y1 == y2:
        print(0, x1, y1)
        continue
    x1, x2 = ord(x1)-64, ord(x2)-64
    y1, y2 = int(y1), int(y2)
    diagonal = [[], []]
    for idx, x, y in ([[0, x1, y1], [1, x2, y2]]):
        for nx, ny in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            d = 1
            while 1 <= x + nx*d <= 8 and 1 <= y + ny*d <= 8:
                diagonal[idx].append((x + nx*d, y + ny*d))
                d += 1
        if idx == 0:
            if (x2, y2) in diagonal[idx]:
                print(1, chr(x1+64), y1, chr(x2+64), y2)
                break
        else:
            inter = set(diagonal[0]).intersection(set(diagonal[1]))
            if inter:
                x3, y3 = list(inter)[0]
                print(2, chr(x1+64), y1, chr(x3+64), y3, chr(x2+64), y2)
            else:
                print("Impossible")
