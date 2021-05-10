class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        check = [True]*n
        for i in range(n):
            for j in range(i+1,n):
                if check[i] and check[j]:
                    a,b,c,d = intervals[i][0], intervals[i][1], intervals[j][0], intervals[j][1]
                    if c <= a and b <= d:
                        check[i] = False
                        break
                    elif a <= c and d <= b:
                        check[j] = False
        
        return check.count(True)