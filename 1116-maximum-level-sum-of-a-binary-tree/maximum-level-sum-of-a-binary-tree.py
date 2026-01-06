# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_of_nodes_at_level = []

        def dfs(node, level, sum_of_nodes_at_level):
            if node is None:
                return 
            if len(sum_of_nodes_at_level) == level:
                sum_of_nodes_at_level.append(node.val)
            else:
                sum_of_nodes_at_level[level] += node.val
            dfs(node.left, level + 1, sum_of_nodes_at_level)
            dfs(node.right, level + 1, sum_of_nodes_at_level)
        dfs(root, 0, sum_of_nodes_at_level)

        max_sum = float("-inf")
        ans = 0

        for i in range(len(sum_of_nodes_at_level)):
            if max_sum < sum_of_nodes_at_level[i]:
                max_sum = sum_of_nodes_at_level[i]
                ans = i + 1
        return ans