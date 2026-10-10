
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the smallest maximum difference we can achieve
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, x - mid) for x in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce every difference to at most left
        remaining = k
        for i in range(len(diff)):
            if diff[i] > left:
                remaining -= diff[i] - left
                diff[i] = left

        # Use leftover operations to reduce some values by one more
        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == left and diff[i] > 0:
                diff[i] -= 1
                remaining -= 1

        return sum(x * x for x in diff)