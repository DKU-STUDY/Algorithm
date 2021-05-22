#dictionary 사용법
#https://dojang.io/mod/page/view.php?id=2308

#Counter 사용법
#https://www.daleseo.com/python-collections-counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for (i,v) in Counter(nums).most_common()[:k]]