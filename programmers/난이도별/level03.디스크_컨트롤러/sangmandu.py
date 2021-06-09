'''
https://programmers.co.kr/learn/courses/30/lessons/42627
디스크 컨트롤러
[풀이]
1. 요청이 먼저 왔어도 수행시간이 짧은 것을 택해야 하기 때문에 우선순위 큐 사용
2. 각 요청별 걸린 시간을 result에 담아서 sum(result)를 반환
=> 따라서 while문은 len(result)가 총 요청의 개수와 같을 때 까지 작동
3. 대기열이 있다면 가장 최근 요청이 걸리는 시간을 time에 더해준다
4. 대기열이 없다면 jobs에서 제일 먼저 실행되는 요청이 시작되는 시간을 time으로 설정
'''
from queue import PriorityQueue

def solution(jobs):
    size = len(jobs)
    jobs.sort(reverse=True)
    waiting = PriorityQueue()
    time = 0
    result = []

    while len(result) < size:
        while jobs and jobs[-1][0] <= time:
            req, spend = jobs.pop()
            waiting.put((spend, req))

        if not waiting.empty():
            spend, req = waiting.get()
            time += spend
            result.append(time - req)
        else:
            time = jobs[-1][0]

    return sum(result) // size
'''
'''