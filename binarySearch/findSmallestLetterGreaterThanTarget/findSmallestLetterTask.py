class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if letters[mid] == target: # если нашли таргет
                if letters[mid + 1] == letters[mid]: # смотрим чтоб не повторялся
                    left = mid
                else:
                    return letters[mid + 1]
            elif letters[mid] > target:
                right = mid
            elif letters[mid] < target:
                left = mid
        resultPos = left if target < letters[left] else right
        if letters[resultPos] == target and resultPos == len(letters) - 1 or target > letters[resultPos]:
            resultPos = 0
        return letters[resultPos]


x = Solution()
# ans = x.nextGreatestLetter(["c", "f", "j"], 'a')
# print(ans)
# ans = x.nextGreatestLetter(["c", "f", "j"], 'd')
# print(ans)
# ans = x.nextGreatestLetter(["c", "f", "j"], 'k')
# print(ans)
ans = x.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], 'e')
print(ans)

