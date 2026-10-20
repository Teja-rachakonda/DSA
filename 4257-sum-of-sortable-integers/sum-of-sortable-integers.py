class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            arr = []

            for start in range(0, n, k):
                block = nums[start:start + k]

                # Find the rotation that makes this block sorted
                drops = 0
                drop_index = -1

                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        drops += 1
                        drop_index = i

                if drops > 1:
                    break

                if drops == 1:
                    block = block[drop_index + 1:] + block[:drop_index + 1]

                arr.extend(block)

            else:
                if arr == sorted(nums):
                    ans += k

        return ans