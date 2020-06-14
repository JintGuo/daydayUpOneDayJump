# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def subcheck(self, A, B):
        if not A:
            return False
        if A.val != B.val:
            return False
        if B.left:
            if not self.subcheck(A.left, B.left):
                return False
        if B.right:
            if not self.subcheck(A.right, B.right):
                return False
        return True

        
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if A.val == B.val:
            if self.subcheck(A, B):
                return True
        if A.left:
            if self.isSubStructure(A.left, B):
                return True
        if A.right:
            if self.isSubStructure(A.right, B):
                return True
        return False
