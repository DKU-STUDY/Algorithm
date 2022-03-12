start_hour, start_minute = map(int, input().split())
need_minute = int(input())
end_minute, need_hour = (start_minute + need_minute) % 60, (start_minute + need_minute) // 60
end_hour = (start_hour + need_hour) % 24
print(end_hour, end_minute)