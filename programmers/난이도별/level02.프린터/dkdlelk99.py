def solution(priorities, location):
    prioritiesMax = max(priorities)
    bool_list = [False]*len(priorities)
    bool_list[location] = True
    count = 0

    while True:
        if priorities[0] < prioritiesMax:
            priorities.append(priorities.pop(0))
            bool_list.append(bool_list.pop(0))
        else:
            count += 1
            priorities.pop(0)
            if bool_list.pop(0):
                return count
            prioritiesMax = max(priorities)

print(solution([2,1,3,2], 2) == 1)
print(solution([1,1,9,1,1,1], 0) == 5)
