def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if(arr[i]!=arr[i-1]):
            answer.append(arr[i])
    # print(answer)
    return answer


print(
    solution([1, 1, 3, 3, 0, 1, 1]),
    solution([1, 1, 3, 3, 0, 1, 1])==[1, 3, 0, 1],
    solution([4, 4, 4, 3, 3]),
    solution([4, 4, 4, 3, 3])==[4, 3]
)
