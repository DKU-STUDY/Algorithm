#n source destination other
def tower_of_hanoi(n:int, source:int, destination:int, other:int):
    if n == 0:
        return
    
    tower_of_hanoi(n-1, source, other, destination)
    answer.append([source,destination])
    tower_of_hanoi(n-1,other,destination,source)


def solution(n):
    global answer
    answer = []
    tower_of_hanoi(n,1,3,2)
    return answer