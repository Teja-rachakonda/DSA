
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Each node stores:
        # total sum, sum of squares, and pending lazy update.
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1
            old_sum = tree_sum[node]

            tree_sq[node] = (
                tree_sq[node]
                + 2 * delta * old_sum
                + delta * delta * length
            ) % MOD

            tree_sum[node] = (
                old_sum + delta * length
            ) % MOD

            lazy[node] += delta

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return tree_sq[node]

            push(node, left, right)
            mid = (left + right) // 2
            result = 0

            if ql <= mid:
                result += query(node * 2, left, mid, ql, qr)

            if qr > mid:
                result += query(node * 2 + 1, mid + 1, right, ql, qr)

            return result % MOD

        last = {}
        answer = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)

            # Increase distinct counts for affected starting positions.
            update(1, 0, n - 1, prev + 1, r)

            # Add squares for every subarray ending at r.
            answer = (
                answer + query(1, 0, n - 1, 0, r)
            ) % MOD

            last[x] = r

        return answer
