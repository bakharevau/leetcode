class Solution:
    def search(self, nums: list[int], leftB, rightB):
        if len(nums) == 0: #частные случаи
            return -1
        if len(nums) == 1:
            return 0

        if nums[0]>nums[1]: #случаи на границах
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1

        left, right = leftB, rightB
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                return Solution.search(self, nums, left, mid)
            else:
                return Solution.search(self, nums, mid + 1, right)

        # Post-processing:
        # End Condition: left == right
        # if left != len(nums) and nums[left] == target:
        #     return left
        # return -1

    def findPeakElement(self, nums: list[int]) -> int:
        return Solution.search(self, nums, 0, len(nums) - 1)


x = Solution()
#ans = x.findPeakElement([1, 2, 1, 3, 5, 6, 4])  # 5
ans = x.findPeakElement([1, 2, 3, 1])
print(ans)
