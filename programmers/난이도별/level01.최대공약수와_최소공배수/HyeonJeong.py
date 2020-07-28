def solution(n, m):
    answer = []
    j = m
    i = n
    while (n % i != 0 or m % i != 0):
        i -= 1
    answer.append(i)
    while (j % n != 0 or j % m != 0):
        j += 1
    answer.append(j)
    return answer

print(solution(3, 12) == [3, 12])