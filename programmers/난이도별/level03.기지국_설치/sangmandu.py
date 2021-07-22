'''
https://programmers.co.kr/learn/courses/30/lessons/12979
기지국 설치
[풀이]
1. 앞쪽 station 부터 얻기 위해 reverse
=> reverse 하지 않으려면 deque 사용도 가능
2. 기지국의 수용 범위 stat을 정의
3. 처음 시작지점은 1
4. 시작지점에서 station의 수용 범위 전까지 필요한 기지국 개수 조사
=> end - w : 기지국 수용범위 가장 처음
=> end - w - start : 기지국이 필요한 아파트 수
5. 다음 시작지점은 end + w + 1 로 잡는다
=> end + w 까지가 기지국 수용범위 끝
6. 마지막 station 수용범위가 아파트 끝이 아니라면 그 사이까지 조사
'''
def solution(n, stations, w):
    stations = stations[::-1]
    stat = 2 * w + 1
    start = 1
    answer = 0
    while stations:
        end = stations.pop()
        cnt = end - w - start
        if cnt > 0:
            answer += (cnt - 1) // stat + 1
        start = end + w + 1

    if start <= n:
        answer += (n - start) // stat + 1

    return answer
'''
'''