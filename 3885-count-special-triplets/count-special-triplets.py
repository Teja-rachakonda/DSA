class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL  = 100000

        suffix_counts = [0] * (MAX_VAL + 1)
        for num in nums:
            suffix_counts[num] += 1
        prefix_counts = [0] * (MAX_VAL + 1)
        total_triplets = 0
        for num in nums:
            suffix_counts[num] -= 1
            target = num * 2

            if target <= MAX_VAL:
                left_matches = prefix_counts[target]
                right_matches = suffix_counts[target]

                if left_matches > 0 and right_matches > 0:
                    total_triplets = (total_triplets + left_matches * right_matches) % MOD
            prefix_counts[num] += 1
        return total_triplets