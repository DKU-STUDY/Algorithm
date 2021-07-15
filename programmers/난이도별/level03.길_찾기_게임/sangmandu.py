'''
https://programmers.co.kr/learn/courses/30/lessons/42892
길 찾기 게임
[풀이]
0. 이진트리 구현 및 탐색
1. 클래스로 이진트리 구현
=> 여기서는 idx와 val값 두개를 가지고 있는 것이 차이점
2. 재귀 제한을 풀지 않으면 5, 6번 문제에서 런타임 에러
3. nodeinfo에서 idx값을 알 수 있도록 추가
4. 주어진 nodeinfo를 y 값에 대해 내림차순 정렬
=> 깊이가 낮은 순으로 트리에 쌓이게 함
=> 트리는 입력 순서에 따라 내용이 달라지기 때문에 깊이 순으로 정렬
'''
class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, val, idx):
        cur_node = self.root
        while True:
            if cur_node.val < val:
                if cur_node.right != None:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = Node(val, idx)
                    break
            else:
                if cur_node.left != None:
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = Node(val, idx)
                    break

    def preorder(self, cur_node):
        if cur_node == None:
            return []
        return [cur_node.idx] + self.preorder(cur_node.left) + self.preorder(cur_node.right)

    def postorder(self, cur_node):
        if cur_node == None:
            return []
        return self.postorder(cur_node.left) + self.postorder(cur_node.right) + [cur_node.idx]


def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10 ** 6)

    nodes = [[idx] + info for idx, info in enumerate(nodeinfo, 1)]
    nodes.sort(key=lambda x: x[2], reverse=True)

    root = Node(nodes[0][1], nodes[0][0])
    tree = Tree(root)

    for node in nodes[1:]:
        tree.insert(node[1], node[0])

    return [tree.preorder(root), tree.postorder(root)]
'''
클래스로 풀어보는 첫 문제.
구현이 번거롭지만 구현하고 나니 풀기는 쉬웠다.
'''