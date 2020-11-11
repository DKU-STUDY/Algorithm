#시도
'''
def solution(n):
    answer = [2]
    for x in range(3, n + 1, 2):
        if x == 3:
            answer.append(3)
        else:
            for y in range(3, x, 2):
                if x % y == 0:
                    break
                elif y == x - 2:
                    answer.append(x)
    return len(answer)
'''

# 에라토스테네스의 체 코드로 완성
def solution(n):
    num = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if num[i] == True:
            for j in range(i + i, n + 1, i):
                num[j] = False

    return len([i for i in range(2, n + 1) if num[i] == True])

print(
    solution(10) == 4,
    solution(5) == 3
)