def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

print(
    solution([1, 4, 2], [5, 4, 4])
)
