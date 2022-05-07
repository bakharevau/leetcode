def guess(n):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1: return 1
        # if n == 2: return 1
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 0:
                return mid
            else:
                left = mid + 1



x = Solution()
ans = x.guessNumber(10)
print(ans)
