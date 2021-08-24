class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)

        while begin < end:
            mid = (begin + end) // 2
            cur = nums[mid]

            if (cur < nums[0]) != (target < nums[0]):
                if target < nums[0]:
                    cur = -9876543210
                else:
                    cur = +9876543210

            if cur < target:
                begin = mid + 1
            elif cur > target:
                end = mid
            else:
                return mid

        return -1
