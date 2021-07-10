import datetime


def solution(n, t, m, timetable):
    #시간대로 정렬한다.
    timetable.sort()
    timeformat = "%H:%M"
    last_passenger = "00:00"
    cnt_last_passenger = 0
    bus_time = "09:00"
    
    #str_time에 분을 더한뒤 다시 string으로 반환한다.
    def minute_add(str_time,t):
        str_time = datetime.datetime.strptime(str_time,timeformat) + datetime.timedelta(minutes = t)
        return str_time.strftime(timeformat)
    
    for bus_cnt in range(n):
        #m명 만큼 탑승시킨다.
        for _ in range(m):
            #버스가 도착하고 최대 m명을 탑승시킨다.
            if timetable and bus_time >= timetable[0]:
                #마지막에 탄 손님의 시간이 계산된다.
                last_passenger = timetable.pop(0)
                if bus_cnt == n-1:
                    cnt_last_passenger += 1
                
        #bus시간을 증가시킨다.
        bus_time = minute_add(bus_time,t)
    
    #마지막버스에 모두가 탑승한 경우 맨 마지막 손님보다 1분 일찍 도착한다.
    if cnt_last_passenger == m:
        return minute_add(last_passenger,-1)
    else:
        #마지막버스가 비었다면 마지막버스시간에 도착한다.
        return minute_add(bus_time,-t)

#결론 : 콘은 무조건 버스 막차를 타야한다.
#막차가 빈다고 예측되면 막차 시간에 맞춰나가면 되고.
#막차가 가득찬다고 예측되면 막차를 타는 마지막 손님보다 1분 앞서 타면된다.