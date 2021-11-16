# N : 스위치의 수 / M : 램프의 수
N, M = map(int, input().split())
# 각 스위치가 가지는 램프의 정보
switches = list()
for _ in range(N):
    lamp, *switch = map(int, input().split())
    switches.append(switch)


# 스위치를 하나씩 안켜본다.
for i in range(N): # i는 안켜는 스위치
    lamps = [0 for _ in range(M + 1)]
    for j in range(N): # j는 켜는 스위치
        if i != j:
            for switch in switches[j]:
                lamps[switch] += 1
    for lamp in lamps[1:]:
        if lamp == 0:
            break
    else:
        print(1)
        exit()
print(0)