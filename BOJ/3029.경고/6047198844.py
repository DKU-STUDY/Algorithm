from datetime import datetime

start_time = datetime.strptime(input(), '%H:%M:%S')
end_time = datetime.strptime(input(), '%H:%M:%S')
total_sec = (end_time - start_time).seconds

m, s = divmod(total_sec, 60)
h, m = divmod(m, 60)
# 적어도 1초를 기다린다.
if h == 0 and m == 0 and s == 0:
    h = 24
print('{:02d}:{:02d}:{:02d}'.format(h, m, s))