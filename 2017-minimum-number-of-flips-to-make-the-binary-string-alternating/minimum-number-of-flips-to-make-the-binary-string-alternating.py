class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s_double = s + s
        
        min_flips = float('inf')
        diff1, diff2 = 0, 0
  
        for i in range(len(s_double)):
            
            expected1 = '1' if i % 2 == 0 else '0'
            expected2 = '0' if i % 2 == 0 else '1'
            
            if s_double[i] != expected1: diff1 += 1
            if s_double[i] != expected2: diff2 += 1
            
           
            if i >= n:
                left_idx = i - n
                old_expected1 = '1' if left_idx % 2 == 0 else '0'
                old_expected2 = '0' if left_idx % 2 == 0 else '1'
                
                if s_double[left_idx] != old_expected1: diff1 -= 1
                if s_double[left_idx] != old_expected2: diff2 -= 1
                
            
            if i >= n - 1:
                min_flips = min(min_flips, diff1, diff2)
                
        return min_flips