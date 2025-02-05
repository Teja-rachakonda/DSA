class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexes = []
        
        # Find indices where s1 and s2 differ
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            # If more than two mismatches, return False early
            if len(indexes) > 2:
                return False
        
        # If exactly two differences, check if swapping makes them equal
        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # If no differences, they are already equal
        return len(indexes) == 0