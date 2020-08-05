def solution(x):
    answer=True
    sum=0
    for i in str(x):
        sum+=int(i)
    if x%sum!=0:
        answer=False
    return answer

print(
    solution(12)==True
)
