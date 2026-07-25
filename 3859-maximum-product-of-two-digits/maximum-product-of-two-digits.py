class Solution:
    def maxProduct(self, n: int) -> int:
        first = second = 0

        while n:
            digit = n % 10

            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit

            n //= 10

        return first * second