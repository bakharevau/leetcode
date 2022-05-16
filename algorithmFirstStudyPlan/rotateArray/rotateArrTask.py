class Solution:
    def swap(self, nums: list[int], i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums: list[int], start, finish):
        while start<finish:
            Solution.swap(self, nums, start, finish)
            start += 1
            finish -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        # nums[:] = nums[n-k:] + nums[:n-k] #easy solution
        Solution.reverse(self, nums, 0, len(nums)-1)
        Solution.reverse(self, nums, 0, k - 1)
        Solution.reverse(self, nums, k, len(nums)-1)
        return nums

    # def rotate(self, nums: list[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     if k == 0:
    #         return
    #     k = k % len(nums)
        # nums[:] = nums[n-k:] + nums[:n-k] #easy solution


x = Solution()
ans = x.rotate([1, 2, 3], 2)
print(ans)

ans = x.rotate([1, 2, 3, 4, 5, 6, 7], 3)
print(ans)
