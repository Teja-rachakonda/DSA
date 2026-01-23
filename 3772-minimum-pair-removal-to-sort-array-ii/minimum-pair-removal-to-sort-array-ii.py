import heapq
from typing import List

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.removed = False
        
    # CRITICAL FIX: Allows heapq to compare Nodes if sums are equal
    def __lt__(self, other):
        return self.idx < other.idx

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # 1. Build Doubly Linked List
        nodes = [Node(x, i) for i, x in enumerate(nums)]
        for i in range(n):
            if i > 0: nodes[i].prev = nodes[i-1]
            if i < n - 1: nodes[i].next = nodes[i+1]
            
        # 2. Initialize Heap and Bad Count
        # Heap stores: (sum, original_index, node_reference)
        pq = []
        bad_count = 0
        
        # Helper: checks if a node and its next neighbor are in decreasing order
        def is_bad(node):
            if node and node.next and node.val > node.next.val:
                return 1
            return 0
            
        for i in range(n - 1):
            s = nodes[i].val + nodes[i+1].val
            heapq.heappush(pq, (s, nodes[i].idx, nodes[i]))
            bad_count += is_bad(nodes[i])
            
        ops = 0
        
        # 3. Simulation Loop
        while bad_count > 0 and pq:
            s, idx, left = heapq.heappop(pq)
            
            # --- Validation (Lazy Removal) ---
            # 1. Check if node is removed
            # 2. Check if neighbor exists
            # 3. Check if sum is current (handles stale heap entries)
            if left.removed or left.next is None:
                continue
            if s != left.val + left.next.val:
                continue
                
            right = left.next
            prev = left.prev
            nxt = right.next
            
            # --- Update Bad Count (Remove Old Relations) ---
            if prev: bad_count -= is_bad(prev)
            bad_count -= is_bad(left)
            bad_count -= is_bad(right)
            
            # --- Perform Merge ---
            left.val += right.val   # Update sum
            left.next = nxt         # Update pointer
            if nxt: nxt.prev = left
            right.removed = True    # Mark right as removed
            
            # --- Update Bad Count (Add New Relations) ---
            if prev: bad_count += is_bad(prev)
            bad_count += is_bad(left)
            
            # --- Push New Adjacent Sums to Heap ---
            if prev:
                heapq.heappush(pq, (prev.val + left.val, prev.idx, prev))
            if nxt:
                heapq.heappush(pq, (left.val + nxt.val, left.idx, left))
                
            ops += 1
            
        return ops