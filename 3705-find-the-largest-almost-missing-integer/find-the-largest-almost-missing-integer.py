class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hs = {}
        n = len(nums)
        ans = []
        for x in nums:
            t = 0
            for i in range(n-k+1):
                temp = nums[i:i+k]
                t += temp.count(x)
            if t==1:
                ans.append(x)
        if n==k:
            for i in nums:
                if i in hs:
                    hs[i]+=1
                else:
                    hs[i]=1

            return max(hs)
        if not ans:
            return -1
        return max(ans)
                
                
            