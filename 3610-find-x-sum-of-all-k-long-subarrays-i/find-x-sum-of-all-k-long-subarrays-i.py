class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):  # sliding window
            sub = nums[i:i + k]  # current subarray
            freq = {}
            
            # count frequency
            for num in sub:
                freq[num] = freq.get(num, 0) + 1
            
            # sort by (frequency desc, value desc)
            sorted_items = sorted(freq.items(), key=lambda y: (-y[1], -y[0]))
            
            # pick top x elements
            total = 0
            count = 0
            for val, f in sorted_items:
                if count == x:
                    break
                total += val * f
                count += 1
            
            ans.append(total)
        
        return ans
