class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba = 6
        abc = 6

        for _ in range(n - 1):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD

            aba = next_aba
            abc = next_abc
        return (aba +  abc) % MOD