# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        Q = collections.deque([root])
        
        while Q:
            node = Q.popleft()
            if not node:
                res += "N "
            else:
                res += str(node.val)+" "
                Q.append(node.left)
                Q.append(node.right)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        if data[0] == 'N':
            return None
        root = TreeNode(int(data[0]))
        Q = collections.deque([root])
        idx = 1
        while Q:
            node = Q.popleft()
            if data[idx] != 'N':
                node.left = TreeNode(int(data[idx]))
                Q.append(node.left)
            idx += 1
            if data[idx] != 'N':
                node.right = TreeNode(int(data[idx]))
                Q.append(node.right)
            idx += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))