class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = bin(num2).count('1')
        
        # Create x starting with num1
        x = 0
        # Turn on bits in num1 that minimize the XOR with num1
        for i in range(31, -1, -1):  # Iterate through 32 bits
            if set_bits == 0:
                break
            if (num1 & (1 << i)) != 0:  # Check if the ith bit of num1 is set
                x |= (1 << i)  # Set the ith bit in x
                set_bits -= 1
        
        # If there are still set bits needed, turn on remaining bits starting from LSB
        for i in range(32):  # Iterate through 32 bits from LSB
            if set_bits == 0:
                break
            if (x & (1 << i)) == 0:  # Check if the ith bit of x is unset
                x |= (1 << i)  # Set the ith bit in x
                set_bits -= 1
        
        return x