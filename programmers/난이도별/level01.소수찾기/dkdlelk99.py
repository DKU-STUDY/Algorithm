def solution(n):
    num = {i for i in range(3, n+1, 2)}
    for i in range(3, n+1, 2):
        num -= set(i for i in range(i*2, n+1, i))
    return len(num) + 1

print(solution(5) == 3)
print(solution(10) == 4)
print(solution(20) == 8)
