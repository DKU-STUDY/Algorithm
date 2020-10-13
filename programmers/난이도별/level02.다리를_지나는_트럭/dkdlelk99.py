# 출처 https://programmers.co.kr/learn/courses/30/lessons/42583
# 풀이 by github id : dkdlelk99, dkdlelk99@gmail.com
# 목표 트럭이 다리를 걸리는데 필요한 최소시간 알아내기
# 조건 트럭은 1초에 거리 1씩 이동, 다리위의 트럭의 무게는 weight를 초과할 수 없음, 모든 트럭의 무게는 1 이상 weight 이하
# bridge_length = 다리의 길이(int), weight = 버티는 최대 무게(int), truck_weights = 건너야 할 트럭의 무게(int)들이 담긴 리스트
def solution(bridge_length, weight, truck_weights):
    sec = 0
    on_the_bridge = [0] * bridge_length #FIFO
    while 1:
        sec += 1
        on_the_bridge.pop(0)
        # 대기 트럭 인덱스 에러 때문에 비어있으면 값 0이라고 해버림
        next_truck = truck_weights[0] if truck_weights != [] else 0

        if sum(on_the_bridge) + next_truck <= weight:
        #다음 트럭 올라올수 있을때
            if truck_weights:
                on_the_bridge.append(truck_weights.pop(0))
            else:#마지막일때 실행
                sec += bridge_length - 1
                break
        #다음 트럭 못올라올때
        else:
            on_the_bridge.append(0)
    return sec
print(solution(2,10,[7,4,5,6]), solution(2,10,[7,4,5,6]) == 8)
print(solution(100,100,[10]), solution(100,100,[10]) == 101)
print(solution(100,100,[10]*10), solution(100,100,[10]*10) == 110)
print(solution(5,6,[1,2,3,1,2]), solution(5,6,[1,2,3,1,2]) == 12) #my test case

# 예시
# 초 / 다리를 건넌 트럭 / 다리 위 트럭 / 대기 트럭
# 0	        []              []          [7,4,5,6]
# 1~2       []              [7]         [4,5,6]
# 3         [7]             [4]         [5,6]
# 4         [7]             [4,5]       [6]
# 5         [7,4]           [5]         [6]
# 6~7       [7,4,5]         [6]         []
# 8	        [7,4,5,6]       []          []
