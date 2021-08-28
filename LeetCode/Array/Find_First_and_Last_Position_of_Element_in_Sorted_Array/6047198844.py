class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []

        begin = 0
        end = len(nums)

        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid

        if not nums or begin == len(nums) or nums[begin] != target:
            ans.append(-1)
        else:
            ans.append(begin)

        begin = 0
        end = len(nums)

        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] <= target:
                begin = mid + 1
            else:
                end = mid
        if not nums or begin == 0 or nums[begin - 1] != target:
            ans.append(-1)
        else:
            ans.append(begin - 1)

        return ans