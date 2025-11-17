class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        t = k
        for i in nums:
            if i == 1:
                if t < k:
                    return False
                t = 0
            else:
                t += 1
        return True