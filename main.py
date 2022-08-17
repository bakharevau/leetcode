# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode], valueList: list):
        if root:
            Solution.helper(self, root.left, valueList)
            valueList.append(root.val)
            Solution.helper(self, root.right, valueList)

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        valueList = []
        Solution.helper(self, root, valueList)
        return valueList


treeNode = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(5, None, None), TreeNode(6, None, None))), TreeNode(7, None, None))

x = Solution()
ans = x.preorderTraversal(treeNode)
print(ans)
# ans = x.combine(1, 1)
# print(ans)
