def solution(a):
    answer = []
    answer.append(a[0])
    for i in range(1,len(a)):
        if a[i] != a[i-1]:
            answer.append(a[i])
    return answer
    
a = [1,1,3,3,0,1,1]
print(solution(a))
b = [1,5,2,2,2,4,4,5,5,5,0,9,9]
print(solution(b))
