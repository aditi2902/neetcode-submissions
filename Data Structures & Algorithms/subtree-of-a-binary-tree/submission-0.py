# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        x=False
        y=False
        def solve(root,subRoot): ##check same /equivalent
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val!=subRoot.val:
                return False
            x=solve(root.left,subRoot.left)
            y=solve(root.right,subRoot.right)
            return x and y
        if root is None:
            return False
        if solve(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or ##recurse over the tree to check at any node
                self.isSubtree(root.right, subRoot))
