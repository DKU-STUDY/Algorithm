'''
https://programmers.co.kr/learn/courses/30/lessons/42587
프린터 : pop한 데이터의 우선순위가 낮으면 다시 append
제일 높은 우선순위의 순서를 기록하면서 해당 우선순위를 제일 낮게 만듬
'''

def solution(priorities, location):
    size = len(priorities)
    order = [0] * size
    i, j = 0, 1
    while min(order) == 0:
        if max(priorities) == priorities[i]:
            order[i] = j
            priorities[i] = 0
            j += 1
        i = (i + 1) % sizeㅁㄴㅇ
    return order[location]

'''
any는 iteration 객체에 대해서 하나라도 참이면 참을 반환
all은 iteration 객체에 대해서 모두 참이어야 참을 반환
내 코드보다 수행시간이 빨라서 참고했음
ㅁㄴㅇㅁㄴㅇdef solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''