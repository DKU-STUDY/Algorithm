def solution(progresses, speeds):
    answer = []
    complete = []
    length = len(speeds)

    # 완료 날짜 배열 complete 생성
    # 이건 문제 없음
    for progress in range(length):
        count = 0
        while progresses[progress] < 100:
            progresses[progress] += speeds[progress]
            count += 1
        complete.append(count)
    
    # 위 배열로 답 만들기 아마 여기가 문제?
    count = 0
    
    for i in range(length):
        big = complete[0]
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
