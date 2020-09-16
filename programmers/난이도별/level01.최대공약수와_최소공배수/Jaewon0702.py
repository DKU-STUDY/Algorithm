def solution(n, m):
    p = n * m  # 최소공배수 = 두 자연수의 곱/ 최대공약수
    while n > 0:  # Euclidean Algorithm
        m, n = n, m % n
    return [m, int(p / m)]


print(solution(2, 5) == [1, 10])
print(solution(3, 12) == [3, 12])
