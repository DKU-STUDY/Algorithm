import math


def solution(n, stations, w):
    answer = 0
    able_stations = [1]
    
    for station in stations:
        if able_stations[-1] > station-w-1:
            able_stations.pop()
        else:
            able_stations.append(station-w-1)
        
        able_stations.append(station+w+1)
    
    #마지막이 범위를 넘어선경우
    if able_stations[-1] > n:
        able_stations.pop()
    else:
        able_stations.append(n)
    
    for idx in range(0, len(able_stations), 2):
        start = able_stations[idx] 
        end = able_stations[idx+1]
        r = end - start + 1
        answer += math.ceil(r/(2*w+1))        
        
    return answer