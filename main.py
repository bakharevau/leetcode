class Solution:
    def mostClosestEls(nums, k, x):
        pass

    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return left if nums[left] > nums[right] else right


x = Solution()
# ans = x.findClosestElements([1, 2, 3, 4, 5], 4, 3)
# ans = x.findClosestElements([1], 1, 1)
# ans = x.findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3)
ans = x.findPeakElement([1, 2, 3, 1])
print(ans)
ans = x.findPeakElement([1, 2])
print(ans)
ans = x.findPeakElement([6, 5, 4, 3, 2, 3, 2])
print(ans)
ans = x.findPeakElement([1, 2, 3, 1])
print(ans)