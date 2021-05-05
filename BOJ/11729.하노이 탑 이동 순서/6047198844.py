# 1에 있는 맨밑을 제외한 모든것들을 2에 옮긴다.
# 1에 있는 하나를 3에 옮긴다.
# 2에 있는 모든것들을 3에 옮긴다.

# n개의 ring을 FROM에서 TO로 옮긴다. FROM / TO / OTHERS
# from : 1 to : 3 others : 2

route = []
def move_ring(n: int, source: int, destination: int, other: int):
    if n==0:
        return 0

    res = 0
    res += move_ring(n - 1, source, other, destination)
    
    route.append((source, destination))
    res += 1
    
    res += move_ring(n - 1, other, destination, source)
    return res


n = int(input())
print(move_ring(n, 1, 3, 2))

for i in route:
    print(i[0], i[1])
