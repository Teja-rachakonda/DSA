class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        left = 0
        #ab
        for i in range(len(s)):
            if s[i] == "(" or locked[i] == "0":
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0":
                right += 1
            else:
                right -= 1
            if right < 0:
                return False
        return True

        
            
            