class Solution:
    def binarySearch3(nums, target):
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        firstNumberIndx = 0
        arr = numbers[:]
        arr.pop(firstNumberIndx)
        while Solution.binarySearch3(arr, target-numbers[firstNumberIndx]) == -1:
            firstNumberIndx += 1
            arr = numbers[:]
            arr.pop(firstNumberIndx)
        result = [firstNumberIndx+1, Solution.binarySearch3(arr, target-numbers[firstNumberIndx])+2]
        return result

x = Solution()
ans = x.twoSum([2,7,11,15], 9)
print(ans)

ans = x.twoSum([1,2,3,4,4,9,56,90], 8)
print(ans)
