R, C, N = map(int, input().split())

board = [list(input()) for _ in range(R)]

# 예외처리
# 짝수 일 경우. 전채 폭탄을  프린트한다.
if N % 2 == 0:
    for r in range(R):
        print('O' * C)
else:
    # 초기 세팅 'O'를 0으로 교체.
    # 0초째 -> 설치
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                board[r][c] = 0
    # 1초째 -> 아무것도 안함
    pass

    # 처음 1초 제외 (2초부터 N초 까지)
    for sec in range(2, N+1):
        pass
        # 2초째 -> 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
        # 4초째 -> 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
        if sec % 2 == 0:
            for r in range(R):
                for c in range(C):
                    if board[r][c] == '.':
                        board[r][c] = sec
        # 3초째 -> 폭탄 폭발 / 0초째의 폭탄이 폭발된다.
        # 5초째 -> 폭탄 폭발 / 2초째의 폭탄이 폭발된다.
        else:
            for r in range(R):
                for c in range(C):
                    # 3초 지난 폭탄을 터트린다.
                    if board[r][c] == sec - 3:
                        # 자신을 터트린다.
                        board[r][c] = '.'
                        # 주변을 터트린다.
                        for dr, dc in (-1, 0), (+1, 0), (0, -1), (0, +1):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != sec - 3:
                                board[nr][nc] = '.'
    #output 출력
    for r in range(R):
        for c in range(C):
            if type(board[r][c]) == int:
                print('O', end='')
            else:
                print('.', end='')
        print()
