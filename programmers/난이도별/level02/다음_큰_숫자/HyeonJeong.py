def solution(n):
    binary_n = bin(n)
    num_1 = binary_n.count('1')
    for i in range(1, 1000001-n): #n은 1000000이하의 자연수 이므로
        if bin(n + i).count('1') == num_1:
            return int(n+i)

print(solution(78)==83, solution(15)==23)