'''
https://www.acmicpc.net/problem/1051
숫자 정사각형
[풀이]
1. 가장 큰 정사각형을 찾는것이 목표이므로 큰 변부터 작아지는 방향으로 찾는다
=> 이 때 큰 변은 가로, 세로 두 개의 길이 중 최솟값이다
2. 계산을 편하게 하기 위해 min(n, m)-1을 edge로 지정
=> -1을 하지 않으면 이후 코드의 모든 edge에 -1 을 해줘야 함
=> 나중에 다시 edge+1로 복귀
3. 반복문으로 각 꼭지점 비교
=> 같다면 바로 edge 출력
=> 다르면 edge 값 1 감소
=> 못찾았다면 크기가 1인 정사각형이므로 1 출력
'''
n, m = map(int, input().split())
edge = min(n, m)-1
board = [input() for _ in range(n)]
while edge > 0:
    for y in range(n-edge):
        for x in range(m-edge):
            if board[y][x] == board[y+edge][x] == board[y][x+edge] == board[y+edge][x+edge]:
                print((edge+1)**2)
                exit()
    edge -= 1
print(1)