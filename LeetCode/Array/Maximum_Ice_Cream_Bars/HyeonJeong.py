class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if min(costs) > coins : return 0
        costs.sort()
        result = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                result += 1
            else:
                break
        return result
