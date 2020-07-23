def solution(progresses, speeds):
    answer = []
    complete = []
    length = len(speeds)

    for progress in range(length):
        count = 0
        while progresses[progress] < 100:
            progresses[progress] += speeds[progress]
            count += 1
        complete.append(count)
    
    count = 0
    big = complete[0]
    for i in range(length):
        if big < complete[i]:
            big = complete[i]
            answer.append(count)
            count = 1
        else:
            count += 1
        if i == length -1:
            answer.append(count)
    return answer

print(solution([93,30,55], [1,30,5]) == [2,1])
