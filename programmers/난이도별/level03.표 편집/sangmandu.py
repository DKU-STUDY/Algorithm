'''
https://programmers.co.kr/learn/courses/30/lessons/81303
표 편집
[풀이]
0. 연결리스트 문제
=> 보통 이런문제가 나오면 클래스로 짜는 사람이 있다. 참 대단..
1. 연결리스트를 딕셔너리로 구현한다.
=> i번째 노드는 원소가 2개인 list 타입의 값을 가진다.
=> [0] : left = i-1번째 노드
=> [1] : right = i+1번째 노드
=> 0번 노드와 n-1번 노드는 양쪽 끝에 None을 가지고 있다.
2. 명령어가 C, Z일때를 조건으로 하고 그 외에는 split()을 한다.
2-1. C일 경우
=> rm 리스트에 삭제할 노드의 idx와 left, right를 추가한다.
=> rm 리스트는 추후에 명령어가 Z일 경우 필요
=> 자신의 left 노드와 right 노드를 서로 이어준다
=> 이 때 None일 경우의 예외처리
2.2 Z일 경우
=> 삭제한 노드가 담겨있는 rm 리스트에서 pop
=> 되돌리려는 노드가 가장 마지막 노드일 경우와 아닌 경우를 나눈다.
=> 그리고 자신의 left, right 노드와 자신을 이어준다.
=> 자신의 left, right가 현재 삭제되있을 가능성은?
=> 없다. 왜냐하면 자신이 가장 최근에 삭제된 노드기 때문
=> 자신의 left, right가 삭제되었다면 이미 또 다른 left, right값을 가지고 있을 것임
2.3 U, D 일 경우
=> D면 idx 증가, U면 idx 감소.
=> 연결리스트의 장점이 드러나는 부분
=> 그 외의 방법은 이동하면서 노드가 삭제되었는지 여부를 검사해야한다.
=> 연결리스트는 연결이 안돼있으면 이미 삭제된 것이기 때문에 검사할 필요가 없음.
'''
def solution(n, k, cmd):
    dic = {}
    for i in range(0, n):
        dic[i] = [i-1, i+1]
    dic[0][0] = dic[n-1][1] = None
    rm = []

    for c in cmd:
        if c == "C":
            rm.append([k, dic[k][0], dic[k][1]])
            if dic[k][1] is None:
                k = dic[k][0]
                dic[k][1] = None
            else:
                if dic[k][0] is not None:
                    dic[dic[k][0]][1] = dic[k][1]
                dic[dic[k][1]][0] = dic[k][0]
                k = dic[k][1]
        elif c == "Z":
            idx, left, right = rm.pop()
            if left is not None:
                dic[left][1] = idx
            if right is not None:
                dic[right][0] = idx
            dic[idx] = [left, right]
        else:
            move, steps = c.split()
            for _ in range(int(steps)):
                k = dic[k][int(move == "D")]

    answer = ["O"] * n
    for idx, _, _ in rm:
        answer[idx] = "X"
    return ''.join(answer)
'''
리스트로 이 문제를 구현하면 100% 시간초과 날 것을 예상했다.
=> 삭제 검사, 리스트 중간에 삽입 및 삭제가 일어날 것이기 떄문
그래서 각 리스트의 상태를 기억할 수 있도록 구조를 짰다. 굉장히 좋은 풀이라고 생각했는데 효율성에서 에러가 났다. (아마 실제 인턴십 코테에서도 저랬던 것 같다)
아래 코드는 리스트로 짠 코드. 4개의 테스트 케이스에서 시간초과가 나서 결국 버려야 했다 ㅠㅠ

def solution(n, k, cmd):
    lst = ["O"] * n
    top = n-1
    remove = []
    for c in cmd:
        if c == "C":
            remove.append(k)
            lst[k] = "X"
            drt = 2 * (top != k) - 1
            while lst[k+drt] == "X":
                k += drt
            k += drt
            while lst[top] == "X":
                top -= 1
        elif c == "Z":
            idx = remove.pop()
            lst[idx] = "O"
            top = max(idx, top)
        else:
            move, steps = c.split()
            steps = int(steps)
            drt = 2 * (move == "D") - 1
            while steps:
                k += drt
                steps -= lst[k] == "O"

        #print(c, lst, remove, top, k)
    
    return ''.join(lst)
'''