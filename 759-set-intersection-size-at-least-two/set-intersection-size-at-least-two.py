class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))
        p1 = -1
        p2 = -1
        ans = 0

        for s, e in intervals:
            is_p1_inside = (s <= p1 <= e)
            is_p2_inside = (s <= p2 <= e)

            count = 0
            if is_p1_inside: count += 1
            if is_p2_inside: count += 1

            if count == 0:
                ans += 2
                p1 = e - 1
                p2 = e

            elif count == 1:
                ans += 1
                p1 = p2
                p2 = e
        return ans