class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                val = i*i + j*j
                c = int(math.sqrt(val))
                if c*c == val and c <= n:
                    count+= 2
        return count