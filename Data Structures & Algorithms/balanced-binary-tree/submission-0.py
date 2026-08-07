class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True

        def solve(root):
            if root is None:
                return 0

            lh = solve(root.left)
            rh = solve(root.right)

            if abs(lh - rh) > 1:
                self.balanced = False

            return 1 + max(lh, rh)

        solve(root)
        return self.balanced