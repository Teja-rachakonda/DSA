class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        seen_A = set()  # Tracks elements seen so far in A
        seen_B = set()  # Tracks elements seen so far in B
        ans = []
        common_count = 0  # Tracks the count of common elements
        
        for i in range(len(A)):
            # If A[i] is in seen_B, it means it's a common element
            if A[i] in seen_B:
                common_count += 1
            seen_A.add(A[i])  # Add A[i] to seen_A
            
            # If B[i] is in seen_A, it means it's a common element
            if B[i] in seen_A:
                common_count += 1
            seen_B.add(B[i])  # Add B[i] to seen_B
            
            # Append the current common count to the result
            ans.append(common_count)
        
        return ans
