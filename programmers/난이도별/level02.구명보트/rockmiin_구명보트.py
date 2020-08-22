def solution(people, limit):
    answer=0
    people.sort(reverse=True)
    rear=len(people)-1
    for i in range(len(people)):
        if people[i]+people[rear]<=limit:
            rear-=1;
        answer+=1
        if i >= rear: break;
    return answer

print(
    solution([70, 50, 80, 50], 100),
    solution([70, 80, 50], 100)
)
