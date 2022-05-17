class Solution:
    def swap(self, arr: list[str], i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            Solution.swap(self, s, left, right)
            left += 1
            right -= 1
        return s


x = Solution()
ans = x.reverseString(["h", "e", "l", "l", "o"])
print(ans)

ans = x.reverseString(["H", "a", "n", "n", "a", "h"])
print(ans)
