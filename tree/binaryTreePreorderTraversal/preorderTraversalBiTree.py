# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        valueList = []
        nodeList = []
        visitedNodes = []
        currentRoot = root
        nodeList.append(currentRoot)
        if currentRoot.left:
            nodeList.append(currentRoot)
            currentRoot = currentRoot.left
            Solution.preorderTraversal(self, currentRoot)
        elif currentRoot.right:
            nodeList.append(currentRoot)
            currentRoot = currentRoot.right
            Solution.preorderTraversal(self, currentRoot)
        else:
            valueList.append(currentRoot.val)
            visitedNodes.append(currentRoot)
            currentRoot = nodeList.pop()
            if currentRoot.left in visitedNodes or currentRoot.left is None:
                currentRoot.left = None
            else:
                currentRoot = currentRoot.left
                Solution.preorderTraversal(self, currentRoot)
            if currentRoot.right in visitedNodes or currentRoot.right is None:
                currentRoot.right = None
            else:
                currentRoot = currentRoot.right
                Solution.preorderTraversal(self, currentRoot)
        return valueList
