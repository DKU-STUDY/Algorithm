def solution(routes):
    routes.sort(key=lambda route: route[1])
    
    pos_camera = -30001
    cnt_camera = 0
    
    for route in routes:
        if pos_camera < route[0]:
            pos_camera = route[1]
            cnt_camera += 1
    return cnt_camera