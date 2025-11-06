from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ----- DSU (Disjoint Set Union) -----
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n + 1))
                self.rank = [0] * (n + 1)
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return
                if self.rank[rx] < self.rank[ry]:
                    self.parent[rx] = ry
                elif self.rank[rx] > self.rank[ry]:
                    self.parent[ry] = rx
                else:
                    self.parent[ry] = rx
                    self.rank[rx] += 1

        # ----- Step 1: Build DSU -----
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # ----- Step 2: Group stations by component -----
        comp_stations = {}
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp_stations.setdefault(root, []).append(i)

        # ----- Step 3: Create heaps for each component -----
        comp_heap = {}
        for root, nodes in comp_stations.items():
            heapq.heapify(nodes)
            comp_heap[root] = nodes

        offline = set()
        res = []

        # ----- Step 4: Process queries -----
        for typ, x in queries:
            if typ == 1:  # Maintenance check
                if x not in offline:
                    res.append(x)
                else:
                    root = dsu.find(x)
                    heap = comp_heap[root]
                    # Remove offline stations from heap top
                    while heap and heap[0] in offline:
                        heapq.heappop(heap)
                    if not heap:
                        res.append(-1)
                    else:
                        res.append(heap[0])
            else:  # Station goes offline
                offline.add(x)

        return res
