def solution(n):
    return "수박" * int(n // 2) + "수" * int(n % 2)


print(solution(3) == "수박수")
print(solution(4) == "수박수박")
