# Задание
Given an array of integers nums sorted 
in non-decreasing order, find the starting 
and ending position of a given target value.

If target is not found in the array, return 
```[-1, -1]```.

You must write an algorithm with ```O(log n)```
runtime complexity.

 

### Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
### Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
### Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
 ```

### Constraints:

+ 0 <= nums.length <= 105
+ -109 <= nums[i] <= 109
+ nums is a non-decreasing array.
+ -109 <= target <= 109

### Костылизм по решению:
Разбил решение на 2 задачи: поиск левой границы,
поиск правой границы.

Появились исключения (крайние, частные случаи), когда элемент только 1, 
так как использовал Template #3, а в нём выход из
цикла случается когда left + 1 -й элемент является
right элементом (между левой и правой границей нет 
элемента)