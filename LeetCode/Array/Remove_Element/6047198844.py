class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #try:
        #    while True:
        #        nums.remove(val)
        #except ValueError:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
        

#참고 
#https://hashcode.co.kr/questions/1158/%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%95%88%EC%97%90-%ED%8A%B9%EC%A0%95%EA%B0%92%EC%9D%84-%EB%8B%A4-%EC%A7%80%EC%9A%B0%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%B4-%EA%B6%81%EA%B8%88%ED%95%A9%EB%8B%88%EB%8B%A4