class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        max_y = 0
        
        for x, y, l in squares:
            total_area += l * l
            max_y = max(max_y, y + l)

        def area_below(line_y):
            area = 0
            for x, y, l in squares:
                if line_y > y:
                    height = min(line_y - y, l)
                    area += height * l
            return area

        lo, hi = 0.0, float(max_y)
        eps = 1e-6

        while hi - lo > eps:
            mid = (lo + hi) / 2
            if area_below(mid) >= total_area / 2:
                hi = mid
            else:
                lo = mid

        return hi
