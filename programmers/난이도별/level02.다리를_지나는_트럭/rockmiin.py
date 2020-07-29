def solution(bridge_length, weight, truck_weight):
    on_bridge=[]
    cnt=[0]* len(truck_weight)
    total_time=1
    pass_truck_count=0
    while truck_weight!=[]:
        if sum(on_bridge)+truck_weight[0]<=weight:
            on_bridge.append(truck_weight.pop(0))
        for i in range(pass_truck_count, pass_truck_count+len(on_bridge)):
            cnt[i]+=1
            if bridge_length==cnt[i]:
                on_bridge.pop(0); pass_truck_count+=1
        total_time += 1
    return total_time+bridge_length-1


print(
    solution(2, 10, [7, 4, 5, 6])==8
)