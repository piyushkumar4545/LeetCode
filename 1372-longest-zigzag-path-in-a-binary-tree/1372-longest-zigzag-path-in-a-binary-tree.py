
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            l = 1 + right[1]
            r = 1 + left[0]

            ans = max(ans, l, r)

            return (l, r)

        dfs(root)
        return ans