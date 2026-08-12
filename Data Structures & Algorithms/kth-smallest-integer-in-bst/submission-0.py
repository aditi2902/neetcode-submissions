# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder is always ascending so return k-1th element
        def inorder(root):
            if root is None:
                return []
            left=inorder(root.left)
            right=inorder(root.right)
            return left+[root.val]+right
        l=inorder(root)
        return l[k-1]


            

            
        
