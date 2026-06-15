# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])
        while q:
            if curr := q.popleft():
                curr.right, curr.left = curr.left, curr.right
                q.extend([curr.left, curr.right])
        return root