import collections

def solution(maps):
    answer = 1
    
    n = len(maps) - 1
    m = len(maps[0]) - 1
    
    #바로 도착인 경우
    if n == 0 and m == 0:
        return answer
    
    discovered = set()
    Q = collections.deque()
    discovered.add((0, 0))
    Q.append((0, 0))
    
    
    while Q:
        answer += 1
        for _ in range(len(Q)):        
            y, x = Q.popleft()
            for dy, dx in (-1, 0), (+1, 0), (0, -1), (0, +1):
                ny = y + dy
                nx = x + dx
                #딥
                if ny == n and nx == m:
                    return answer
                
                #범위 / 벽 / 발견 X
                if 0 <= ny <= n and 0 <= nx <= m and maps[ny][nx] != 0 and (ny, nx) not in discovered:
                    discovered.add((ny, nx))
                    Q.append((ny, nx))
        
    return -1

#deque.rotate(num)