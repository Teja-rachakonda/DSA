
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
       
        sorted_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
       
        def build_balanced_tree(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            
          
            mid = (left_idx + right_idx) // 2
            node = sorted_nodes[mid]
            
        
            node.left = build_balanced_tree(left_idx, mid - 1)
            node.right = build_balanced_tree(mid + 1, right_idx)
            
            return node
            
        return build_balanced_tree(0, len(sorted_nodes) - 1)