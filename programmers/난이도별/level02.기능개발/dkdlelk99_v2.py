from collections import deque
def solution(progresses, speeds):
    answer = []
    Q = deque([])
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        if progresses[i] >= 100:
            Q.append(count)
            
    count = 1
    first = Q.popleft()
    for i in range(len(Q)):
        compare = Q.popleft()
        if first >= compare:
            count += 1
        else:
            answer.append(count)
            count = 1
            first = compare
        if Q ==[]:
            break
    answer.append(count)
    return answer
print(solution([93,30,55], [1,30,5]), solution([93,30,55], [1,30,5]) == [2,1])
print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]),\
      solution([95,90,99,99,80,99], [1,1,1,1,1,1]) == [1,3,2])
