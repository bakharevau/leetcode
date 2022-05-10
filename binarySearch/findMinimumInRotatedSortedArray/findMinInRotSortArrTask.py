class Solution:
    def rotatePivotIndexSearch(self, nums):  # возвращает
        if len(nums) == 0:
            return -1
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 1
            else:
                return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:  # сравниваем окрестность mid-1, mid, mid+1
                return mid
            elif nums[mid + 1] < nums[mid]:
                return mid + 1
            elif nums[mid] < nums[left]:  # сравниваем края left, mid, right
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return -1
        return -1

    def findMin(self, nums: list[int]) -> int:
        index = Solution.rotatePivotIndexSearch(self, nums)
        if index == -1:
            return nums[0]
        else:
            return nums[index]


x = Solution()
# ans = x.rotatePivotIndexSearch([4, 5, 6, 7, 0, 1, 2])
# ans = x.search([4, 5, 6, 7, 0, 1, 2], 0)
# print(ans)
#ans = x.rotatePivotIndexSearch([3, 4, 5, 1, 2])
ans = x.findMin([3, 4, 5, 1, 2])
print(ans)
ans = x.findMin([10, 1, 10, 10, 10])
print(ans)