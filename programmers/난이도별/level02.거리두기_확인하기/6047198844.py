import collections
def bfs(table):
    for y in range(0,5):
        for x in range(0,5):
            #bfs시작
            if table[y][x] == 'P':
                Q = collections.deque([(y,x)])
                discovered = set()
                discovered.add((y,x)) #조심
                cnt = 0
                while Q:
                    cnt += 1
                    for _ in range(len(Q)):
                        yy, xx = Q.popleft()
                        for dy, dx in (-1,0), (+1,0), (0,-1),(0,+1):
                            ny = yy + dy
                            nx = xx + dx
                            if 0 <= ny < 5 and 0 <= nx < 5 and (ny,nx) not in discovered:
                                discovered.add((ny,nx))
                                if table[ny][nx] == 'O':
                                    Q.append((ny,nx))
                                elif table[ny][nx] == 'P' and cnt <= 2:
                                    return 0
    return 1
                                

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))    
    return answer