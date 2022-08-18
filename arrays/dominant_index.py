class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        arr = nums[:]
        arr.sort()
        if arr[len(arr)-1] >= 2*arr[len(arr)-2]:
            return nums.index(arr[len(arr)-1])
        return -1


x = Solution()

ans = x.dominantIndex([3, 6, 1, 0])
print(ans)

ans = x.dominantIndex([1, 2, 3, 4])
print(ans)