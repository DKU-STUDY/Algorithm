import collections

def solution(dirs):
    answer = 0
    
    position = (0, 0)
    
    table = {
        'U' : (-1, 0),
        'D' : (+1, 0),
        'L' : (0, -1),
        'R' : (0, +1)
    }
    
    
    res = set()
    
    for dir in dirs:
        y, x= position
        dy, dx = table[dir]
        ny, nx = y + dy, x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            nposition = (ny, nx)
            res.add((position, nposition))
            res.add((nposition, position))
            position = nposition
    
    return len(res) // 2