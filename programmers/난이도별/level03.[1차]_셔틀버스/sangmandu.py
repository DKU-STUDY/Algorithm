'''
https://programmers.co.kr/learn/courses/30/lessons/17678
[1차] 셔틀버스
[풀이]
1. 시간 문제라서 import time을 할까 했지만 직접 만지는게 편해 보임
=> 각 시간 "hh:mm"을 [hh, mm] 로 변환
2. 시간 역순으로 정렬한다.
=> 가장 먼저 온 사람부터 태우기 위함
3. board에 가장 먼저 온 사람부터 태울 것이다.
=> 다 태우면(len(board) < m) 다음 차가 올 것이다(for num in range(n):)
=> 단, 셔틀이 오기전까지 도착한 사람만 태울 것이다(if timetable[-1][0] < hour or timetable[-1][0] == hour and timetable[-1][1] <= minute:)
=> 근데 셔틀이 오기전에 도착한 사람이 없으면 그냥 출발할 것이다(break)
4. 마지막 board만을 확인한다.
=> 콘은 제일 늦게 타야 하므로. 마지막 board만 확인
5. 마지막 셔틀에 자리가 있으면 그냥 탑승. 그렇지 않으면 가장 마지막에 탄 사람보다 1분만 빨리 기다리면 되지 않겠나?
=> 마지막에 탄 사람보다 1분만 빠르면 된다. (문제 조건은 00:01 부터 23:59 이므로 하루가 넘어가는 예외처리는 필요없음)
6. 이 때 여러 경우의 수를 생각해 볼 수 있다.
[9시, 9시 1분, 9시 2분] => 9시 1분에 오면 된다.
[9시, 9시, 9시] => 8시 59분에 오면 된다.
[9시, 9시], [9시 10분, 9시 10분] => 9시 9분에 오면 된다.
=> 이 때 마지막 셔틀을 타는 것은 아니기 때문에
=> "콘이 셔틀을 타고 사무실로 갈 수 있는도착 시간 중 제일 늦은 시각" 조건을 깨는 것이 아닐까라는 생각할 수 있다.
=> 그러나 가장 마지막 셔틀을 타지 않더라도 그 전 셔틀을 타는것이 콘이 사무실로 갈 수 있는 제일 늦은 셔틀이다.
7. 실제로 시간과 분을 int형태로 변환했으므로 "9:5" 를 "09:05" 로 변환할 수 있도록 한다.
'''
def solution(n, t, m, timetable):
    timetable = sorted(list(map(lambda x: [int(x[:2]), int(x[3:])], timetable)))[::-1]

    for num in range(n):
        hour, minute = 9 + (num * t) // 60, (num * t) % 60
        board = []
        while len(board) < m and timetable:
            if timetable[-1][0] < hour or timetable[-1][0] == hour and timetable[-1][1] <= minute:
                board.append(timetable.pop())
                continue
            break

    if len(board) >= m:
        l_hour, l_minute = board[-1]
        hour, minute = l_hour - int(l_minute - 1 < 0), ((l_minute - 1) + 60) % 60

    hour, minute = "0" + str(hour) if hour < 10 else hour, "0" + str(minute) if minute < 10 else minute
    return f"{hour}:{minute}"
'''
'''