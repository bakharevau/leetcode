class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        zrsCount = 0
        while (n - i) > zrsCount:
            if nums[i] == 0:
                zrsCount += 1
                nums.pop(i)
                nums.append(0)
                if i != 0:
                    i -= 1
            else:
                i += 1
        return nums


x = Solution()
ans = x.moveZeroes([0, 1, 0, 3, 12])
print(ans)

ans = x.moveZeroes([0,0,1])
print(ans)
