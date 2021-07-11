#다시풀어보기. 실수가 많았다.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


def solution(n, k, cmds):
    answer = ''

    begin = cur = Node(None)

    # 이중연결리스트 형식으로 표현
    prev = Node(None)
    for i in range(n):
        cur.next = Node(i)
        cur.next.prev, cur = cur, cur.next


    # begin은 현재 맨앞을 가리킨다.
    #begin = 
    cur = begin.next
    #맨 앞을 삭제하더라도 . 삭제가 안됨.
    
    # 삭제한 노드.
    # 문제였음
    delete_node = []

    # cur 은 현재 커서이다. k만큼 이동시킨다.
    for _ in range(k):
        cur = cur.next

    # 명령 수행한다.
    for cmd in cmds:
        # C 또는 Z
        if len(cmd) == 1:
            # C인경우. 행이 하나도 남지않는 경우는 없다.
            # 삭제할 노드의 이전노드와 삭제할 노드의 다음노드를 연결한다.
            if cmd == 'C':
                delete_node.append(cur)
                prev_node = cur.prev
                next_node = cur.next
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                    cur = next_node
                else:
                    cur = prev_node
            # Z인경우
            # 복구한다.
            # 현재 선택된 행은 바뀌지 않는다.
            else:
                #문제였음.
                recover_delete_node = delete_node.pop()
                delete_prev_node = recover_delete_node.prev
                delete_next_node = recover_delete_node.next
                if delete_prev_node:
                    delete_prev_node.next = recover_delete_node
                if delete_next_node:
                    delete_next_node.prev = recover_delete_node
        # U 또는 D
        else:
            cmd, X = cmd.split()
            # U인경우
            if cmd == 'U':
                for _ in range(int(X)):
                    cur = cur.prev
            # D인경우
            else:
                for _ in range(int(X)):
                    cur = cur.next

    cur = begin
    answer = ['O' for _ in range(n)]
    
    #delete_node에서 삭제한 노드를 계산
    for node in delete_node:
        answer[node.data] = 'X'
        
        
    return ''.join(answer)