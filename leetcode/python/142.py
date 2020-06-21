# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # O(n)
        # 以root为端点的最大路径： root, root + l, root + r
        maxPath = [-2**31]
        def maxPathSumWithRoot(root):
            if not root:
                return 0
            lSum = maxPathSumWithRoot(root.left)
            rSum = maxPathSumWithRoot(root.right)
            maxPath[0] = max(maxPath[0], max(lSum,0)+root.val+max(rSum,0))
            return root.val + max(lSum, rSum, 0)
        maxPathSumWithRoot(root)
        return maxPath[0]
