def solution(priorities, location):
    original=0
    while(priorities!=[]) :
        m=max(priorities)
        p=priorities.pop(0)
        if p<m :
            priorities.append(p)
            location = location - 1 if location > 0 else len(priorities)-1
            continue
        original+=1                      #이 이후로는 https://somjang.tistory.com/155를 참고하였다.
        if location == 0 :
            break
        else :
            location-=1

    return original 

print(solution([2,2,2,1,3,4],3)==6)
print(solution([2,1,3,2], 2) == 1)
print(solution([1,1,9,1,1,1], 0) == 5)

#100점 
