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

# реализация Template #3 для задачи поиска пикового значения