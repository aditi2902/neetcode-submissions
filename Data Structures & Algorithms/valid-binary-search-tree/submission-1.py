class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, low, high):

            if root is None:
                return True

            if root.val <= low or root.val >= high:
                return False

            left = check(root.left, low, root.val)
            right = check(root.right, root.val, high)

            return left and right

        return check(root, float('-inf'), float('inf'))