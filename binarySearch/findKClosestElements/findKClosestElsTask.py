class Solution:
    def mostClosestEls(nums, k, x):
        result = []
        count = 0
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == x:
                left = mid - 1
                right = mid + 1
                break
            elif nums[mid] < x:
                left = mid
            else:
                right = mid
        # нашли границы
        mid = (left + right) // 2  # в случае подачи на вход массива из 1 или 2х элементов
        if nums[mid] == x:
            result.append(nums[mid])
            count += 1

        while count < k:
            if left != -1 and right != -1:
                if abs(nums[left] - x) <= abs(nums[right] - x):
                    result.insert(0, nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1
                    if right == len(nums): right = -1  # выход за пределы массива
            elif left == -1 and right != -1:
                result.append(nums[right])
                right += 1
                if right == len(nums): right = -1
            elif right == -1 and left != -1:
                result.insert(0, nums[left])
                left -= 1
            count += 1

        return result

    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        return Solution.mostClosestEls(arr, k, x)


x = Solution()
ans = x.findClosestElements([1, 2, 3, 4, 5], 4, 3)
ans = x.findClosestElements([1], 1, 1)
ans = x.findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3)

print(ans)
