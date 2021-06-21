'''
https://programmers.co.kr/learn/courses/30/lessons/42628
이중우선순위큐
[풀이]
1. 우선순위 큐 라이브러리 호출
2. 최솟값을 제거할 경우 => heappop 이용
3. 최댓값을 제거할 경우 => nlargest 이용
'''
from heapq import heappush, heappop, nlargest
def solution(operations):
    que = []
    for o in operations:
        com, num = (lambda x : (x[0], int(x[1])))(o.split())
        if com == 'I':
            heappush(que, num)
        else:
            if num == 1:
                que = nlargest(len(que), que)[1:][::-1]
            else:
                if len(que) > 0:
                    heappop(que)
    return (lambda x : [x[-1], x[0]] if len(x) > 0 else [0, 0])(sorted(list(que)))
'''
시간초과에 예민한 문제가 아니라 풀어도 찝찝하다.
이런 문제는 최대최소힙을 선언 후 동기화하는 과정으로 풀고 싶었다.
최대최소힙에 대한 비슷한 문제가 있어서 풀었던 것으로 기억하는데,
무슨 문제였는지 기억이 잘 안난다.

새로 알게된 문법
heapq.remove(value) : 해당 값을 삭제
heapq.nlargest(length, heap) : heap에서 크기가 큰 순으로 해당 길이만큼 반환.
'''