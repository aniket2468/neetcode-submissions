# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        if root is None:
            return 0
        
        leftHeight, rightHeight = self.Height(root.left), self.Height(root.right)

        if leftHeight < 0 or rightHeight < 0 or abs (leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1