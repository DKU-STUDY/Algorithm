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



print(
    solution(10) == 4,
    solution(5) == 3
)