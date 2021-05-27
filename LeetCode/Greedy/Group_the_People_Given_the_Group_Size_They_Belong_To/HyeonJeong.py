class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        order_s = [[] for x in range(max(groupSizes))]
        result = []
        for i, x in enumerate(groupSizes):
            order_s[x-1] += [i]
        for i, n in enumerate(order_s):
            length = len(n)
            if length == i+1:
                result.append(n)
            if length > i+1:
                index = 0
                for j in range(int(length/(i+1))):
                    result.append(n[index:index+(i+1)])
                    index += i+1
        return result
