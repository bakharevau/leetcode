class Solution(object):
    def findMin(self, nums):
        min = nums[0]
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
        return min
        # if len(nums) == 1:
        #     return nums[0]
        #
        # left = 0
        # right = len(nums) - 1
        #
        # if nums[right] > nums[0]:
        #     return nums[0]
        #
        # while right >= left:
        #     mid = left + (right - left) // 2
        #     if nums[mid] > nums[mid + 1]:
        #         return nums[mid + 1]
        #     if nums[mid - 1] > nums[mid]:
        #         return nums[mid]
        #
        #     if nums[mid] > nums[0]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        #
        # return 0


x = Solution()
ans = x.findMin([2, 2, 2, 0, 1])
print(ans)
