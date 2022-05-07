def guess(n):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
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