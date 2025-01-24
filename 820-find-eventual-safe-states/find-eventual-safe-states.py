from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # Step 1: Build the reverse graph and calculate in-degrees
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
                in_degree[node] += 1
        
        # Step 2: Collect terminal nodes (nodes with zero in-degree)
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Step 3: Perform BFS to determine all safe nodes
        safe_nodes = set()
        while queue:
            node = queue.popleft()
            safe_nodes.add(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
    
        return sorted(safe_nodes)

        