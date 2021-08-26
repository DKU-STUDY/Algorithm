class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals = sorted(intervals, key=lambda L: (L[0], -L[1]))
        print(intervals)

        for nbegin, nend in intervals:
            if not ans:
                ans.append([nbegin, nend])
            else:
                # 가장 최근에 추가된 interval
                rbegin, rend = ans[-1]

                # 교집합을 구한다.
                # 교집합이 없는 경우
                if rend < nbegin:
                    ans.append([nbegin, nend])
                # 교집합이 있는 경우
                else:
                    ans.pop()
                    # 포함되는 경우.
                    if nend <= rend:
                        ans.append([rbegin, rend])
                    # 교집합이 있는 경우.
                    else:
                        ans.append([rbegin, nend])
        return ans