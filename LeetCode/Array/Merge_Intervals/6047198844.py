class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda L: (L[0], -L[1]))
        for nbegin, nend in intervals:
            #ans가 없는 경우 && 교집합이 없는 경우
            if not ans or ans[-1][1] < nbegin:
                ans.append([nbegin, nend])
            else:
                # 교집합을 구한다.
                # 교집합이 있는 경우
                # 포함되는 경우.
                ans[-1][1] = ans[-1][1] if nend <= ans[-1][1] else nend
        return ans