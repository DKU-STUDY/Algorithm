def solution(a, b):
    sum=0
    for i in range(a if a<b else b, a+1 if a>b else b+1):
        sum+=i
    return sum

print(solution(3, 5),
     solution(3, 5)==12,
     solution(5, 3),
     solution(5, 3)==12
     )