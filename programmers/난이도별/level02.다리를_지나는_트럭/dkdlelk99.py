def solution(bridge_length, weight, truck_weights):
    sec = 0
    on_the_bridge = [] #FIFO
    while 1:
        sec += 1
        if truck_weights != []:
            next_truck = truck_weights[0]
        else:
            next_truck = 0

        if sum(on_the_bridge) + next_truck <= weight:
            if truck_weights == []:
                sec += bridge_length - 2
                on_the_bridge.clear()
            else:
                on_the_bridge.append(truck_weights.pop(0))
        else:
            sec += bridge_length - 2
            on_the_bridge.clear()
        if truck_weights == [] and on_the_bridge == []:
            break
    return sec + 1
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10]*10))
