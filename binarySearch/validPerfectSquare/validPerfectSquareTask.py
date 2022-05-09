class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        if num == 1: return True
        while left < right:
            mid = (left + right)//2
            calcVal = mid*mid
            if calcVal <= num < (mid + 1)*(mid + 1):
                if calcVal == num:
                    return True
                else:
                    return False
            elif calcVal > num:
                right = mid
            else:
                left = mid
        return -1



x = Solution()
ans = x.isPerfectSquare(16)
print(ans)
ans = x.isPerfectSquare(15)
print(ans)
ans = x.isPerfectSquare(100)
print(ans)
ans = x.isPerfectSquare(1)
print(ans)