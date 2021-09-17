class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = 1
        while root**2 < num:
            root += 1
        return root**2 == num