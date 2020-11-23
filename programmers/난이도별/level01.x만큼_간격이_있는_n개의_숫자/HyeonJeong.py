#방법1
def solution(x, n):
    if x == 0 :
        return [0] * n
    return [a for a in range(x, x * n + x, x)]

#방법2
def solution(x, n):
    return [x * a for a in range(1, n + 1)]

print(
    solution(2, 5) == [2,4,6,8,10],
    solution(4, 3) == [4,8,12],
    solution(-4, 2) == [-4, -8]
)