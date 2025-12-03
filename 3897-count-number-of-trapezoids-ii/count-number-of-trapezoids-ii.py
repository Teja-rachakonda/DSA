import math
from collections import defaultdict
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        def get_slope_and_line(p1, p2):
            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]

            g = math.gcd(dy, dx)
            dy //= g
            dx //= g

            if dx < 0:
                dy, dx = -dy, -dx
            elif dx == 0:
                dy = abs(dy)

            line_c = dx * p1[1] -dy * p1[0]
            return (dy, dx), line_c

        slope_map = defaultdict(lambda: defaultdict(int))
        midpoint_map = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                slope, line_c = get_slope_and_line(p1, p2)
                slope_map[slope][line_c] += 1
                mid_x, mid_y = p1[0] + p2[0], p1[1] + p2[1]
                midpoint_map[(mid_x, mid_y)][slope] += 1
        total_trapezoids = 0

        for slope, lines_dict in slope_map.items():
            total_segments = sum(lines_dict.values())
            if total_segments < 2:
                continue
            all_pairs = total_segments * (total_segments - 1) // 2
            same_line_pairs = 0
            for count in lines_dict.values():
                same_line_pairs += count * (count - 1) // 2
            total_trapezoids += (all_pairs - same_line_pairs)
        total_parallelograms = 0
        for mid, slopes_dict in midpoint_map.items():
            total_segments = sum(slopes_dict.values())
            if total_segments < 2:
                continue

            all_pairs = total_segments * (total_segments - 1) // 2
            same_slope_pairs = 0
            for count in slopes_dict.values():
                same_slope_pairs += count * (count - 1) // 2
            total_parallelograms += (all_pairs - same_slope_pairs)
        MOD = 10**9 + 7
        return (total_trapezoids - total_parallelograms) % MOD