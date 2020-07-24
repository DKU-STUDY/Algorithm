def solution(priorities, location):
    answer=0

    while True:
        if priorities[0] == max(priorities):
            answer+=1; priorities.pop(0)
            if location==0: return answer
            else: location-=1
        else:
            priorities.append(priorities.pop(0))
            if location==0: location=len(priorities)-1
            else: location-=1
    return answer

print(
    solution([2, 1, 3, 2], 2)==1
)
