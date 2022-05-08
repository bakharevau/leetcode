class Solution:
    def rotatePivotIndexSearch(self, nums): #возвращает
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
            if nums[mid] < nums[mid - 1]: #сравниваем окрестность mid-1, mid, mid+1
                return mid
            elif nums[mid+1] < nums[mid]:
                return mid+1
            elif nums[mid] < nums[left]: #сравниваем края left, mid, right
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return -1
        return -1

    def binarySearch(self, nums, target, pivotIndex):
        if pivotIndex == -1: #если нет ротации, устанавливаем границы как обычно
            left, right = 0, len(nums) - 1
        else: #если есть ротация, проверяем в какой промежуток входит наш таргет
            if nums[0] <= target <= nums[pivotIndex - 1]:
                left, right = 0, pivotIndex - 1
            else:
                left, right = pivotIndex, len(nums) - 1

        if len(nums) == 0: # частные случаи
            return -1
        elif len(nums) == 1 and nums[0] == target:
            return 0

        while left <= right: #сам бинарный поиск
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums: list[int], target: int) -> int:
        pivotIndex = Solution.rotatePivotIndexSearch(self, nums)
        return Solution.binarySearch(self, nums, target, pivotIndex)


x = Solution()
# ans = x.rotatePivotIndexSearch([4, 5, 6, 7, 0, 1, 2])
ans = x.search([4, 5, 6, 7, 0, 1, 2], 0)
print(ans)
ans = x.search([4, 5, 6, 7, 0, 1, 2], 0)
# ans = x.search(10)
print(ans)
