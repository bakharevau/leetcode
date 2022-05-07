class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    left = mid
            else:
                right = mid
        return -1


x = Solution()
ans = x.mySqrt(4)
print(ans)
