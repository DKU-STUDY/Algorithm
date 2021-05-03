class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        result = 0
        check = [0]*len(light) # 노란색으로 변한(켜진) 전구는 1, 꺼진 전구는 0
        max_index = 0 # 불이 켜진 전구 중 가장 오른쪽에 있는 전구의 번호(1~5)
        for i, x in enumerate(light):
            if x > max_index:
                max_index = x
            check[x-1] = 1
            if max_index <= i+1 and sum(check[:max_index]) == max_index:
                # 왼쪽이 연속적으로 켜져서 파란색으로 변하는 경우
                result += 1
        return result
