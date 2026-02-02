import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Base cost is always nums[0]
        base_cost = nums[0]
        n = len(nums)
        
        # Target size for the 'left' heap (smallest elements)
        target = k - 1
        
        # Heaps
        left = []  # Max-heap (store negative values)
        right = [] # Min-heap
        
        # State tracking
        current_sum = 0
        left_count = 0  # Number of elements physically in left heap logic
        
        # Lazy deletion maps
        # out_map tracks elements that have left the window but are still in heaps
        out_map_left = defaultdict(int)
        out_map_right = defaultdict(int)
        
        # CRITICAL FIX: Track how many instances of 'v' are strictly in the Left Heap
        L_frequency = defaultdict(int)

        def balance():
            nonlocal current_sum, left_count
            
            # 1. Clean tops of heaps
            while left and out_map_left[-left[0]] > 0:
                out_map_left[-left[0]] -= 1
                heapq.heappop(left)
            while right and out_map_right[right[0]] > 0:
                out_map_right[right[0]] -= 1
                heapq.heappop(right)
                
            # 2. If left is too small, fill from right
            while left_count < target and right:
                val = heapq.heappop(right)
                # Check if this popped value was actually a "deleted" one
                if out_map_right[val] > 0:
                    out_map_right[val] -= 1
                    continue
                
                heapq.heappush(left, -val)
                current_sum += val
                left_count += 1
                L_frequency[val] += 1
                
                # Clean left top after push (just in case)
                while left and out_map_left[-left[0]] > 0:
                    out_map_left[-left[0]] -= 1
                    heapq.heappop(left)

            # 3. If left is too big, move to right (unlikely if logic is tight, but safe)
            # Or if invariant broken: max(left) > min(right)
            while (left and right and -left[0] > right[0]) or (left_count > target):
                # We need to move top of left to right
                val = -heapq.heappop(left)
                if out_map_left[val] > 0:
                    out_map_left[val] -= 1
                    continue
                    
                current_sum -= val
                left_count -= 1
                L_frequency[val] -= 1
                
                heapq.heappush(right, val)
                
                # Re-clean right
                while right and out_map_right[right[0]] > 0:
                    out_map_right[right[0]] -= 1
                    heapq.heappop(right)

        def add(val):
            nonlocal current_sum, left_count
            # Always push to left first, then let balance() sort it out
            heapq.heappush(left, -val)
            current_sum += val
            left_count += 1
            L_frequency[val] += 1
            balance()

        def remove(val):
            nonlocal current_sum, left_count
            # CRITICAL FIX: Use L_frequency to decide where to remove from
            if L_frequency[val] > 0:
                # It is in the left heap
                L_frequency[val] -= 1
                current_sum -= val
                left_count -= 1
                out_map_left[val] += 1
            else:
                # It is in the right heap
                out_map_right[val] += 1
            balance()

        # --- Sliding Window Logic ---
        
        # Window constraints:
        # We are looking at nums[1:]. The window length is dist + 1.
        # We need to find the minimum sum of k-1 smallest elements in windows of size dist+1.
        
        # Initial Window
        # The window spans indices 1 to dist + 1 inside the original array.
        # Ensure we don't go out of bounds if n is small.
        limit = min(n, dist + 2) 
        for i in range(1, limit):
            add(nums[i])
            
        min_total = base_cost + current_sum
        
        # Slide
        # We remove nums[i] and add nums[i + dist + 1]
        # range starts at 1 because that's the start of our sliding area
        # The first element to REMOVE is nums[1] when we slide to the next step.
        
        for i in range(1, n - (dist + 1)):
            out_val = nums[i]
            in_val = nums[i + dist + 1]
            
            remove(out_val)
            add(in_val)
            
            min_total = min(min_total, base_cost + current_sum)
            
        return min_total