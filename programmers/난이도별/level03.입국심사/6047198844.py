def solution(n, times):
    answer = 0
    
    min_time = 1
    max_time = max(times)*n
    
    left = min_time
    right = max_time
    
    while left < right:
        mid = (left + right) // 2
        complete_person_n = 0
        for time in times:
            complete_person_n +=  mid //time
        
        if complete_person_n >= n:
            right = mid
        else:
            left = mid + 1
    
    answer = left
    return answer