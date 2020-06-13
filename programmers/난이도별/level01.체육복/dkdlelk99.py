def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n - len(lost_set)
    

print(solution(6, [1,2,3,4,5,6], [1,3]) == 2)
print(solution(5, [2, 4], [1, 3, 5]) == 5)    
