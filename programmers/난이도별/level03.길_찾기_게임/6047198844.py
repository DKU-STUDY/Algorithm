import collections
import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
        
def solution(nodeinfo):
    nodeinfo = collections.deque(sorted(list(enumerate(nodeinfo, start=1)), key=lambda node:(-node[1][1],node[1][0])))
    #node data는 번호, [x,y]로 이루어진다.
    root = None
    
    def insert(cur, node):
        if cur is None:
            cur = node
        else:
            if cur.data[1][0] > node.data[1][0]:
                cur.left = insert(cur.left, node)
            else:
                cur.right = insert(cur.right, node)
        return cur
                
    while nodeinfo:
        node = nodeinfo.popleft()
        root = insert(root, Node(node))
    
    preorder_list = []
    def preorder(root):
        if root:
            preorder_list.append(root.data[0])
            preorder(root.left)
            preorder(root.right)
    preorder(root)
    
    
    postorder_list = []
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            postorder_list.append(root.data[0])
    postorder(root)
    
    return [preorder_list,postorder_list]