def solution(n):
    if n % 2 == 0:
        return "수박" * (n//2)
    elif n % 2 == 1:
        return "수" + "박수" * (n//2)

print(solution(6) == '수박수박수박')
print(solution(11) == '수박수박수박수박수박수')
