class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        n = len(nums)

        # Sort by digit sum, then by number
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index
        target = {num: i for i, num in enumerate(arr)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps