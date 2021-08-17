'''
n = 1 =>  1 '()'
n = 2 => (1) / 1 '()()' => 2
n = 3 => (2) /  1*2-1, 2*1-1 / 1 '()()()' => 2 + 2 + 1 '()()()'=> 5

카탈랑수
'''


def solution(n):
    answer = 0

    memo = [0] * (n + 1)

    # C_0 == 1
    memo[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(i, j, i - 1 - j)
            memo[i] += memo[j] * memo[i - 1 - j]
            print(memo)

    return memo[n]