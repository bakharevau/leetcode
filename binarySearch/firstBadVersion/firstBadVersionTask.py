# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0:
            return -1

        if n == 1:
            return 1

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            ibv = isBadVersion(mid)
            if ibv:
                right = mid
            else:
                left = mid + 1

        if isBadVersion(left):
            return left
        return -1

x = Solution()
ans = x.firstBadVersion(5)
