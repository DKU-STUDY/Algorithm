class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    # x와 y가 주어졌을 때, bound와 작거나 같은 x**i + y**j의 결과를 리스트로 반환하는 문제
        result = []
        if bound < 2:
            return result
        if x > y:
            x,y = y,x
        m = 0 # y의 제곱수
        if x == 1 and y == 1:
            return [2]
        elif x == 1:
            while (y**m + 1<= bound):
                result += [y**m+1]
                m += 1
            return result
        n = 0
        while (y**m <= bound):
            while (y**m + x**n <= bound):
                result += [y**m + x**n]
                n += 1
            n = 0
            m += 1
        return set(result)
