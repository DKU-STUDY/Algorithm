def solution(progresses, speeds):
    length = len(progresses)
    list = []
    answer = []
    for i in range(length):
        list.append((100 - progresses[i])//speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[i])//speeds[i] + 1) # list에 배포가 될 때까지 기다려야 하는 일수
    for i, x in enumerate(list):
        if x == 0: #앞의 것과 같은 날에 배포될 수 있는 경우
            continue
        answer.append(1)
        for j in range(i + 1, length): # length = len(list)
            if list[i] >= list[j]:
                list[j] = 0
                answer[-1] += 1
            else:
                break
    return answer

print(
    solution([93, 30, 55], [1, 30, 5]) == [2, 1],
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
)
