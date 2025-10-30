class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(0, target[i] - target[i - 1])
        return ans