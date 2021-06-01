import collections


def D(N):
    return 2 * N % 10000


def S(N):
    return 9999 if N == 0 else N - 1


def L(N):
    return (N % 1000) * 10 + N // 1000


def R(N):
    return (N // 10) + (N % 10) * 1000


def bfs(A, B):
    if A == B:
        return 0

    # (숫자, 버튼 경로) 저장
    Q = collections.deque()
    Q.append((A, ""))
    # 발견한 숫자 저장.
    discovered = set()
    discovered.add(A)

    button_cnt = 0
    while Q:
        button_cnt += 1
        for _ in range(len(Q)):
            a, button_path = Q.popleft()
            for button, na in zip(('D', 'S', 'L', 'R'), (D(a), S(a), L(a), R(a))):
                if na in discovered:
                    continue
                n_button_path = button_path + button
                if na == B:
                    return n_button_path
                Q.append((na, n_button_path))
                discovered.add(na)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
