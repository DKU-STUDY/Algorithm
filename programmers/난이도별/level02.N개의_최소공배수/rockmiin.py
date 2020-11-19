def minimize(x, y):
    for i in range(y, (x+1) * y, y):
        if i % x == 0:
            return i

def solution(arr):
    answer=1
    arr= sorted(arr)

    for i in range(len(arr)):
        answer= minimize(answer, arr[i])
    return answer

solution([2, 6, 8, 14])
