class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        A_values = set()
        B_values = set()
        count = 0
        ans = []
        for i in range(len(A)):
            if A[i] in B_values:
                count += 1
            A_values.add(A[i])
            if B[i] in A_values:
                count += 1
            B_values.add(B[i])
            ans.append(count)
        return ans
            