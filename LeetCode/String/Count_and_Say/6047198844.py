class Solution:
    def countAndSay(self, n: int) -> str:
        #연속된 횟수 / 연속된수
        res = ['1']
        for _ in range(n-1):
            prev = res[0]
            cnt = 0
            tmp = []
            for num in res:
                if num == prev:
                    cnt += 1
                else:
                    tmp.append(str(cnt))
                    tmp.append(prev)
                    cnt = 1
                    prev = num
                    
            tmp.append(str(cnt))
            tmp.append(prev)
            res = tmp
            
        return ''.join(res)
                    