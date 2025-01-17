class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0
        for i in derived:
            if i == 1:
                last = ~last
            else:
                last = last
        return first == last