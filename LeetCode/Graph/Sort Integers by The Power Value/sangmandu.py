'''
https://leetcode.com/problems/sort-integers-by-the-power-value/
Graph : 시행 한 결과를 매번 cache에 저장하여 속도 향상
'''

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ans = []
        cache = {}
        for o_num in range(lo, hi + 1):
            num = o_num
            prior = []
            cnt = 0
            while num != 1:
                cnt += 1
                if num in cache:
                    cnt += cache[num]
                    break
                prior.append(num)
                num = 3 * num + 1 if num % 2 else num // 2

            ans.append((cnt, o_num))
            for ele in prior:
                cnt -= 1
                cache[ele] = cnt

        return sorted(ans)[k - 1][1]

'''
'''