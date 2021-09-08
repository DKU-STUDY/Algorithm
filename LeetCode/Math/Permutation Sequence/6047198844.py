class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = map(str,range(1,n+1))
        cnt = 1
        for i in permutations(s):
            if k == cnt:
                return ''.join(i)
            cnt += 1