# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        first Bad Version을 찾아라.
        1, 2, 3, 4, 5, ... , n 이 있다고 해보자.

        이분탐색 -> lower bound

        '''
        begin = 0
        end = n + 1
        # true가 처음으로 들어갈 공간을 찾는다.
        while begin < end:
            mid = (begin + end) // 2
            # mid가 현재 false이다.
            if not isBadVersion(mid):
                begin = mid + 1
            else:
                end = mid
        return begin