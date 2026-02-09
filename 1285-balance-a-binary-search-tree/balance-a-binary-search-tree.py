# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: In-order traversal to get nodes in sorted order
        sorted_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Recursively build the balanced BST from the sorted list
        def build_balanced_tree(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
            # Pick the middle element as the root of this subtree
            mid = (left_idx + right_idx) // 2
            node = sorted_nodes[mid]
            
            # Recursively build left and right subtrees
            node.left = build_balanced_tree(left_idx, mid - 1)
            node.right = build_balanced_tree(mid + 1, right_idx)
            
            return node
            
        return build_balanced_tree(0, len(sorted_nodes) - 1)