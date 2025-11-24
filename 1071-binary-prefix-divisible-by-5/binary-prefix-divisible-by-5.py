class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        t = []
        curr = 0
        for i in nums:
            curr = (curr * 2 + i) % 5
            if curr == 0:
                t.append(True)
            else:
                t.append(False)
        return t