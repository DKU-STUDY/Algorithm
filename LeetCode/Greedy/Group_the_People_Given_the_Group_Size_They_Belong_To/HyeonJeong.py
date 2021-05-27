class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        order_s = [[] for x in range(max(groupSizes))]
        result = []
        for i, x in enumerate(groupSizes):
        # 그룹의 크기별로 사람들을 나누는 과정
            order_s[x-1] += [i]
        for i, n in enumerate(order_s):
            length = len(n)
            if length == i+1:
                result.append(n)
            if length > i+1:
                index = 0
                for j in range(int(length/(i+1))):
                # 필요한 크기로 그룹을 쪼개는 과정
                    result.append(n[index:index+(i+1)])
                    index += i+1
        return result
