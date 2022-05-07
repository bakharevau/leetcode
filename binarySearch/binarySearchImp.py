class Solution:
    def search(self, nums: list[int], target: int) -> int:
        leftBorder = 0
        rightBorder = len(nums) - 1
        for i in range(len(nums)):
            if target == nums[leftBorder]:
                return leftBorder
            if target == nums[rightBorder]:
                return rightBorder

            if target == nums[round((leftBorder + rightBorder) / 2)]:
                return round((leftBorder + rightBorder) / 2)

            if target > nums[round((leftBorder + rightBorder) / 2)]:
                leftBorder = round((leftBorder + rightBorder) / 2)

            if target < nums[round((leftBorder + rightBorder) / 2)]:
                rightBorder = round((leftBorder + rightBorder) / 2)
        return -1


# leetCodeVersion
class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        leftBorder = 0
        rightBorder = len(nums) - 1
        while leftBorder <= rightBorder:
            pivot = leftBorder + (rightBorder - leftBorder) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                rightBorder = pivot - 1
            else:
                leftBorder = pivot + 1
        return -1

#templates of BS

#Template #1:
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

x = Solution()
ans = x.search([-1, 0, 3, 5, 9, 12], 9)
print(ans)

