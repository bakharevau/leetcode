class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        list1 = nums1
        list2 = nums2
        list1.sort()
        list2.sort()
        n = len(list1) if len(list1) > len(list2) else len(list2)
        list1Bigger = True if len(list1) > len(list2) else False
        if list1Bigger:
            for i in range(n):
                if list1[i] in list2 and list1[i] not in result:
                    result.append(list1[i])
        else:
            for i in range(n):
                if list2[i] in list1 and list2[i] not in result:
                    result.append(list2[i])
        return result