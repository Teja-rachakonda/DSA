class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) - k + 1 < need:
            return False
        seen = set()
        for i in range(len(s) - k + 1):
            sub = s[i : i + k]
            seen.add(sub)
            if len(seen) == need:
                return True
        return len(seen) == need