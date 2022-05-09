class Solution:
    def search(self, nums: list[int], target: int) -> int:
        leftBorder = 0
        rightBorder = len(nums) - 1
        for i in range(len(nums)):
            if target == nums[leftBorder]:
                return leftBorder
            if target == nums[rightBorder]:
                return rightBorder

            if target == nums[round((leftBorder + rightBorder) / 2)]:
                return round((leftBorder + rightBorder) / 2)

            if target > nums[round((leftBorder + rightBorder) / 2)]:
                leftBorder = round((leftBorder + rightBorder) / 2)

            if target < nums[round((leftBorder + rightBorder) / 2)]:
                rightBorder = round((leftBorder + rightBorder) / 2)
        return -1


# leetCodeVersion
class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        leftBorder = 0
        rightBorder = len(nums) - 1
        while leftBorder <= rightBorder:
            pivot = leftBorder + (rightBorder - leftBorder) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                rightBorder = pivot - 1
            else:
                leftBorder = pivot + 1
        return -1

#templates of BS

#Template #1:
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

#Template #2:
def binarySearch2(nums, target):
    """
    Шаблон № 2 — это расширенная форма бинарного поиска.
    Он используется для поиска элемента или условия, требующего доступа к
    текущему индексу и индексу его непосредственного правого соседа в массиве.

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1

#Template #3:
def binarySearch3(nums, target):
    """
    Шаблон №3 — еще одна уникальная форма бинарного поиска.
    Он используется для поиска элемента или условия, требующего доступа к
    текущему индексу и его ближайшим левым и правым соседним индексам в массиве.

    Ключевые атрибуты:
    + Альтернативный способ реализации бинарного поиска
    + Условие поиска требует доступа к ближайшим левым и правым соседям элемента.
    + Используйте соседей элемента, чтобы определить, выполняется ли условие, и решить, идти ли влево или вправо
    + Гарантирует, что пространство поиска имеет размер не менее 3 на каждом шаге.
    + Требуется постобработка. Цикл/рекурсия заканчивается, когда у вас остается 2 элемента. Необходимо оценить, соответствуют ли остальные элементы условию.

    Отличительный синтаксис:
    + Начальное состояние: left = 0, right = length-1
    + Прекращение: left + 1 == right
    + Поиск слева: right = mid
    + Поиск справа: left = mid

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
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

x = Solution()
ans = x.search([-1, 0, 3, 5, 9, 12], 9)
print(ans)

