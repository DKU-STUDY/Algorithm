class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(set([tuple(x) for x in intervals])) # 2차원 리스트의 값에서 중복 제거
        intervals = sorted(intervals, key =lambda x: x[0]) # 2차원 리스트의 첫번째 인자 값으로 정렬
        length = len(intervals)

        i = 1
        while i < length:
            if length == 1:
                break

            m = intervals[i-1]
            n = intervals[i]
            if m[0] <= n[0] <= m[1]: # 두 범위에 겹쳐지는 값이 있는지 확인
                for i, cmp in enumerate(intervals): # 합쳐진 리스트가 추가될 위치 확인
                    if cmp[0] > m[0]:
                        index = i-1
                        break
                    elif i == len(intervals)-1:
                        index = len(intervals)

                # 두 리스트가 큰 범위로 합쳐져서 추가됨
                if m[1] <= n[1]:
                    intervals.insert(index, [m[0], n[1]])
                else:
                    intervals.insert(index, [m[0], m[1]])

                intervals.remove(m)
                intervals.remove(n)
                i = 1 # 리스트에 새로운 값이 추가 되었으므로 처음부터 다시 비교
                length = len(intervals)
            else:
                i += 1

        return intervals
