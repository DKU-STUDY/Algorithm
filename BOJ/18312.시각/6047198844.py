# 문제
# 정수 N과 K가 입력되었을 때 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 K가 하나라도 포함되는 모든 시각을 세는 프로그램을 작성하시오. 시각을 셀 때는 디지털 시계를 기준으로, 초 단위로만 시각을 구분한다.
#
# 예를 들어 K=3일 때, 다음의 시각들은 3이 하나 이상 포함되어 있으므로 세어야 하는 시각의 대표적인 예시이다.
#
# 23시 00분 00초
# 07시 08분 33초
# 반면에 다음의 시각들은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 예시이다.
#
# 15시 02분 55초
# 18시 27분 45초
# 입력
# 첫째 줄에 정수 N과 K가 공백을 기준으로 구분되어 주어진다. (0≤N≤23, 0≤K≤9)
#
# 출력
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 K가 하나라도 포함되는 시각들의 수를 출력한다.
from datetime import timedelta, datetime

N, K = input().split()
start_time = datetime(100, 1, 1, 0, 0, 0)
end_time = datetime(100, 1, 1, int(N), 59, 59)

res = 0
while start_time <= end_time:
    res += int(K in start_time.strftime('%H%M%S'))
    start_time += timedelta(seconds=1)
print(res)