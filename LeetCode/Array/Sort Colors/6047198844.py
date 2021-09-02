class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1

        # white를 움직이자
        while white <= blue:
            color = nums[white]
            if color == 1:
                white += 1
            elif color == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1

        return nums