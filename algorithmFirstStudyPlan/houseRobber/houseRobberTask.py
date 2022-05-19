class Solution:
    def rob(self, nums: list[int]) -> int:
        cur_sum = 0
        prev_sum = 0

        for x in nums:
            old_prev_sum = prev_sum #храним значение предыдущего шага
            prev_sum = cur_sum
            if old_prev_sum+x > cur_sum:
                cur_sum = old_prev_sum + x #вычисляем текущее значение по предыдущему значению предыдущего шага

        return cur_sum


x = Solution()
ans = x.rob([1, 2, 3, 1])
print(ans)
ans = x.rob([2, 7, 9, 3, 1])
print(ans)
