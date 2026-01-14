from typing import List
import bisect

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        
        for x, y, l in squares:
            events.append((y, 1, x, x + l))       # add
            events.append((y + l, -1, x, x + l))  # remove
        
        events.sort()
        
        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    total += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            total += cur_r - cur_l
            return total
        
        active = []
        prev_y = events[0][0]
        area_segments = []
        total_area = 0
        
        i = 0
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                width = union_length(active)
                area = width * dy
                if area > 0:
                    area_segments.append((prev_y, y, width, area))
                    total_area += area
            
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1
            
            prev_y = y
        
        target = total_area / 2
        curr = 0
        
        for y1, y2, width, area in area_segments:
            if curr + area >= target:
                return y1 + (target - curr) / width
            curr += area
        
        return prev_y  # fallback (theoretically unreachable)
