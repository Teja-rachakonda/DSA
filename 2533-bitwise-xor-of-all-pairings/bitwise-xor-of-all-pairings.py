class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0
        
        # Calculate XOR of all elements in nums1
        for num in nums1:
            xor1 ^= num
        
        # Calculate XOR of all elements in nums2
        for num in nums2:
            xor2 ^= num
        
        # If nums2 has odd length, each element in nums1 contributes to the result
        # If nums1 has odd length, each element in nums2 contributes to the result
        if len(nums2) % 2 == 0:
            xor1 = 0
        if len(nums1) % 2 == 0:
            xor2 = 0
        
        # XOR the results to get the final answer
        return xor1 ^ xor2