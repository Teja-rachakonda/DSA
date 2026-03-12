from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.comps = n
        
    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.comps -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Pre-check 1: Can the graph be connected at all?
        dsu_all = DSU(n)
        for u, v, s, m in edges:
            dsu_all.union(u, v)
        if dsu_all.comps > 1:
            return -1
            
        # Pre-check 2: Do the mandatory edges form a cycle?
        # A spanning tree cannot contain cycles.
        dsu_must = DSU(n)
        for u, v, s, m in edges:
            if m == 1:
                if not dsu_must.union(u, v):
                    return -1 
                    
        # Filter edges to speed up the binary search checks
        must_edges = []
        free_edges = []
        max_possible_strength = 0
        min_must_strength = float('inf')
        
        for u, v, s, m in edges:
            max_possible_strength = max(max_possible_strength, s * 2)
            if m == 1:
                must_edges.append((u, v, s))
                min_must_strength = min(min_must_strength, s)
            else:
                free_edges.append((u, v, s))
                
        # Helper function to check if a target stability X is achievable
        def check(X: int) -> bool:
            dsu = DSU(n)
            
            # Step 1: Add mandatory edges. If any is < X, this target is impossible.
            for u, v, s in must_edges:
                if s < X:
                    return False
                dsu.union(u, v)
                
            # Step 2: Greedily add free edges that require NO upgrades (cost = 0)
            for u, v, s in free_edges:
                if s >= X:
                    dsu.union(u, v)
                    
            # Step 3: Add free edges that require EXACTLY 1 upgrade (cost = 1)
            upgrades_needed = 0
            for u, v, s in free_edges:
                if s < X and s * 2 >= X:
                    # Only use the upgrade if it connects two different components
                    if dsu.find(u) != dsu.find(v):
                        dsu.union(u, v)
                        upgrades_needed += 1
                        
            # It's valid if all nodes are connected and we didn't exceed the upgrade limit
            return dsu.comps == 1 and upgrades_needed <= k

        # Binary Search for the maximum stability
        low = 0
        
        # The maximum possible answer is bounded by the smallest mandatory edge 
        # (since it cannot be upgraded) or the largest possible upgraded edge.
        high = min(max_possible_strength, min_must_strength if min_must_strength != float('inf') else max_possible_strength)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid       # This stability works, try to push it higher
                low = mid + 1
            else:
                high = mid - 1  # This stability is too high, lower the target
                
        return ans