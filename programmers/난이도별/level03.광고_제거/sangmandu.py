'''
https://programmers.co.kr/learn/courses/30/lessons/72414
광고 제거
[풀이]
1. 시간을 hh:mm:ss 꼴에서 ss꼴로 변환하기
=> 자주 사용하므로 함수화
2. play_time 만큼의 시간 리스트를 생성한다
=> DP 문제이다
3. 각 시간별로 사용자의 시청 시작 시간이 있는 위치에 +1을,
시청 종료 시간이 있는 위치에 -1을 대입한다
4. 이후, 각 시간을 이전 시간과 자신의 합으로 표현한다
=> times[idx] += times[idx-1]
=> 이렇게 되면 각 시간에 시청하고 있는 사용자 수를 알 수 있게 된다
5. 이후, 첫 시간부터 광고시간 만큼 유저수를 비교해서 최대를 파악한다
=> 이 부분도 어려운 아이디어인데, 보통 이 문제를 풀면 총 시간을 세려고 하는데
여기서는 단지 각 시간마다의 유저수를 세는 것이 포인트이다. 유저 수가 곧 1초이므로.
=> 이 때 매번 리스트 sum을 하면 시간 복잡도에 걸리므로 마지막 원소를 추가하고
첫 원소를 제거하는 것도 포인트이다.
6. 좀 더 이해를 돕기위해 카카오 공식 해설 링크를 삽입한다.
https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
'''
def solution(play_time, adv_time, logs):
    spt = lambda x: list(map(int, x.split(':')))
    wsum = lambda y: 3600 * y[0] + 60 * y[1] + y[2]
    trsf = lambda z: wsum(spt(z))

    play, adv = trsf(play_time), trsf(adv_time)
    times = [0] * (play + 1)

    logs = [log.split('-') for log in logs]
    for st, ed in logs:
        times[trsf(st)] += 1
        times[trsf(ed)] -= 1
    for idx in range(1, play):
        times[idx] += times[idx - 1]

    curtime = sum(times[:adv])
    maxidx, maxtime = 0, curtime
    for idx in range(adv, play):
        curtime = curtime + times[idx] - times[idx - adv]
        if maxtime < curtime:
            maxtime = curtime
            maxidx = idx - adv + 1

    return f"{maxidx // 3600:02d}:{maxidx % 3600 // 60:02d}:{maxidx % 60:02d}"
'''
너무 어렵다.. 정답률 1%대 문제일 만 하다..
당시에 나도 시간초과에 벽에 걸렸었는데 이런 아이디어를 생각하지 못했다.
역시 어지간하면 풀이는 쉽다. 어렵게 풀면 내가 잘못가고 있다고 생각해야 할 듯
https://www.youtube.com/watch?v=Yr_xHHNsBog 참고했다
'''