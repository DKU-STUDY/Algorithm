import collections
import heapq

def solution(jobs):
    answer = 0
    N = len(jobs)
    
    jobs.sort()
    
    #현재 시간
    current_sec = 0
    
    #현재 진행중인 작업(들어온시간, 소요시간) , 시작한 시간 (1개 이상)
    current_job = None
    
    #대기 중인 작업들
    PQ = []
    
    #대기시간의 합 / 작업 종료시에 종료시점 - 작업 입력 시점(job)
    waiting_time = 0
    
    #초단위로 상황 접근.
    #대기중인 작업 / 현재 작업이 없을때까지.
    #current_job : 현재 작업의 요청시간, 현재 작업의 시작시간, 현재 작업의 종료시간
    while PQ or current_job or jobs or current_sec == 0:
        #현재시간에 넣을수있는 job들을 PQ에 넣는다.
        while jobs and current_sec == jobs[0][0]:
            #heaq오류 조심?
            request_time, duration = jobs.pop(0)
            #소요시간 / 요청시점
            heapq.heappush(PQ,(duration, request_time))
        
        #현재작업이 있는지. 현재 작업이 종료되는지 여부판단. 현재 작업 종료 시간 == 현재 시간
        if current_job and current_job[2] == current_sec:
            print(current_job)
            request_time, start_sec, end_sec = current_job
            waiting_time += end_sec - request_time
            #작업 종료
            current_job = None

        #현재 작업이 없다면 현재 작업 설정
        if not current_job and PQ:
            #PQ의 맨앞값을 현재 작업으로 지정.
            duration, request_time = heapq.heappop(PQ)
            
            #현재 작업 설정 (요청시간, 시작한 시간, 종료시간)
            current_job = (request_time, current_sec, current_sec + duration)
        
        #1초 증가
        current_sec += 1
    
    return waiting_time // N