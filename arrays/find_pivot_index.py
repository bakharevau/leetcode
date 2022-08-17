class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sums = [0]
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            sums.append(left_sum)

        print(sums)

        for i in range(len(nums)):
            print(sums[i])
            print(sums[len(sums) - 1] - sums[i] - nums[i])
            print('\n')
            if sums[i] == sums[len(sums) - 1] - sums[i] - nums[i]:
                return i

        return -1


x = Solution()

ans = x.pivotIndex([1, 7, 3, 6, 5, 6])
print(ans)

ans = x.pivotIndex([-1, -1, 0, 1, 1, 0])
print(ans)
