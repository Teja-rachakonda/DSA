class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        temp = 0
        for i in patterns:
            if i in word:
                temp += 1
        return temp