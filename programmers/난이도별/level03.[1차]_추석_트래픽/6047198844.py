import datetime
import collections

def solution(lines):
    timetable = list()
    
    #데이터 전처리
    for line in lines:
        date, time, duration = line.split()
        #date 필요없음
        end_time = datetime.datetime.strptime(date + " " + time,"%Y-%m-%d %H:%M:%S.%f").timestamp()
        start_time = end_time - float(duration[:-1]) + 0.001
        timetable.append((start_time, end_time))
    
    
    DQ = collections.deque()
    answer = 1
    
    for start_time, end_time in timetable:
        DQ.append((start_time, end_time))
        
        while DQ and not(start_time - DQ[0][1] <=  0.999):
            DQ.popleft()

        answer = max(answer,len(DQ))
    

    DQ2 = collections.deque()
    timetable.sort()
    
    for start_time, end_time in timetable:
        DQ2.append((start_time, end_time))
        
        while DQ2 and not(DQ2[0][0] <= start_time - 0.999):
            DQ2.popleft()
            
        answer = max(answer,len(DQ2))
    
    return answer