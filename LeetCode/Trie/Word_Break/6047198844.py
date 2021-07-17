
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.check = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    #현재 트라이에 삽입한다.
    def insert(self, word):
        node = self.root
        
        for char in word:
            node = node.children[char]
        node.check = True
     
    #단어가 존재하는지 확인.
    def find(self, word):
        node = self.root
        
        for char in word:
            if char not in word:
                return False
            node = node.children[char]
        
        return node.check
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = Trie()
        for word in wordDict:
            res.insert(word)
        
        #방문했으면 True. 방문했다는것은 해당 인덱스로 접근했을때 답이 아니라는것임.
        N = len(s)
        memo = [False for _ in range(N)]
        
        def dfs(start):
            if N == start:
                return True
            
            if memo[start]:
                return False
            
            for end in range(start + 1, N + 1):
                if res.find(s[start:end]) and dfs(end):
                    return True
            
            memo[start] = True
            return False
        
        return dfs(0)
        