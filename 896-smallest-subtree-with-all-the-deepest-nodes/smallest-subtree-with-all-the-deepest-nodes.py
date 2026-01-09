# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {None: -1}
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        max_depth = max(depth.values())
        def answer(node):
            if not node or depth.get(node) == max_depth:
                return node
            L = answer(node.left)
            R = answer(node.right)
            if L and R: return node
            if L: return L
            if R: return R
            return None
        return answer(root)