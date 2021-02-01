from collections import deque

def solution(numbers, target):
    res= 0
    q= deque([[numbers[0], 0], [-numbers[0], 0]])
    while q:
        x, cnt= q.popleft()
        if cnt==len(numbers)-1 and x==target:
            res+=1
        if cnt < len(numbers) - 1:
            for dx in [-numbers[cnt+1], numbers[cnt+1]]:
                q.append([x+ dx, cnt+1])
                # print([x+dx, cnt+1])
    return res

# numbers=[1, 1, 1, 1, 1]
# target= 3
# print(solution(numbers, target))