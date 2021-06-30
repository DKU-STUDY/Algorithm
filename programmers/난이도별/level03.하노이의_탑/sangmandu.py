'''
https://programmers.co.kr/learn/courses/30/lessons/12946
하노이의 탑
[풀이]
1. n = 1
=> [1, 3]
2. n = 2
=> [1, 2], [1, 3], [2, 3]
3. n = 3
=> [1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]
4. n = 4
=> [1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]
5. 여기까지 규칙을 보면 가장 큰 원판을 옮길 때를 기준으로 양쪽에 규칙이 있다.
=> 큰 원판을 옮기기 전까지는 n-1 에 대해서 1은 고정, 2와 3을 서로 바꾼 순서로 진행.
=> 큰 원판을 옮긴 후에는 n-1 에 대해서 3은 고정, 1과 2를 서로 바꾼 순서로 진행
'''
def solution(n):
    answer = [[1, 3]]
    for _ in range(n - 1):
        front = []
        for hanoi in answer:
            a, b = hanoi
            if hanoi[0] != 1:
                a = 6 // hanoi[0]
            if hanoi[1] != 1:
                b = 6 // hanoi[1]
            front.append([a, b])

        back = []
        for hanoi in answer:
            a, b = hanoi
            if hanoi[0] != 3:
                a = 2 // hanoi[0]
            if hanoi[1] != 3:
                b = 2 // hanoi[1]
            back.append([a, b])
        answer = front + [[1, 3]] + back

    return answer
'''
학부 인공지능 수업에서 하노이를 재귀로 풀었던 기억이 있는데, 까맣게 까먹었다.
다른 사람 풀이 보자마자, 아 맞다! 했다...
재귀로 풀어도 위 로직은 동일하다. (근데 재귀가 더 깔끔하고 직관적)
'''