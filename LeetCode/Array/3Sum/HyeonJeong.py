class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) < 3 :
            return []
        slist = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                for c in nums[i+j+2:]:
                    if a+b+c == 0:
                        if a<=b:
                            if b<=c:
                                slist += [[a, b, c]]
                            elif c<=a:
                                slist += [[c, a, b]]
                            else:
                                slist += [[a, c, b]]
                        else:
                            if a<=c:
                                slist += [[b, a, c]]
                            elif c<=b:
                                slist += [[c, b, a]]
                            else:
                                slist += [[b, c, a]]
        answer = []
        for x in slist:
            if x not in answer:
                answer += [x]
        return answer