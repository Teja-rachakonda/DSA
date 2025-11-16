class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1_000_000_007
        total_count = 0
        current_length = 0
        for char in s:
            if char == "1":
                current_length += 1
            else:
                if current_length > 0:
                    substring_for_block = (current_length * (current_length + 1)) // 2
                    total_count = (total_count + substring_for_block) 

                current_length = 0
        
        if current_length > 0:
            substring_for_block = (current_length * (current_length + 1)) // 2
            total_count = (total_count + substring_for_block) % MOD
        
        return total_count

