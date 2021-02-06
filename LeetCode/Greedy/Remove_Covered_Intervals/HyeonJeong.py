class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        while i+1 < len(intervals):
            n1, n2 = intervals[i]
            for j, [m1, m2] in enumerate(intervals[i+1:]):
                if n1 <= m1 and m2 <= n2:
                    intervals.pop(i+j+1)
                    i -= 1
                    break
                elif m1 <= n1 and n2 <= m2:
                    intervals.pop(i)
                    i -= 1
                    break
            i += 1
        return len(intervals)
