class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for i in range(len(fruits)):
            temp = -1
            for j in range(len(baskets)):

                if fruits[i]<=baskets[j]:

                    baskets[j] = -1
                    temp = 1
                    break

            if temp==-1:
                ans+=1

        return ans