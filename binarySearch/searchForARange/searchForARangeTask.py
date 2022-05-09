class Solution:
    def binarySearchBorder(nums, target, direction=0):  # 0 - leftBorder, 1 - rightBorder
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 2 and nums[0] == nums[1] == target:
            if direction:
                return 1
            else:
                return 0

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if direction:
                    if nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid
                elif not direction:
                    if nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target and direction == 0 or nums[left] == target and nums[right] != target:
            return left
        if nums[right] == target and direction == 1 or nums[right] == target and nums[left] != target:
            return right
        return -1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        leftBorder = Solution.binarySearchBorder(nums, target, 0)
        rightBorder = Solution.binarySearchBorder(nums, target, 1)
        return [leftBorder, rightBorder]


x = Solution()
ans = x.searchRange([5, 8, 8, 8, 8, 10], 8)
ans = x.searchRange([], 8)
ans = x.searchRange([1, 2, 2], 2)
ans = x.searchRange([1, 3], 1)
ans = x.searchRange([1, 4], 4)
print(ans)
