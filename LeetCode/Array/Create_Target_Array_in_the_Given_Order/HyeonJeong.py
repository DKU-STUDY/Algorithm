class Solution:
# nums의 값을 target[nums의 인덱스와 같은 위치의 index값]에 넣어서 리스트를 반환하는 문제
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, n in enumerate(index):
            target = target[:n] + [nums[i]] + target[n:]
        return target
