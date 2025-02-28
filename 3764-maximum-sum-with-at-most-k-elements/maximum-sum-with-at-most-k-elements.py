class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        list = []
        i = 0
        for row in grid:
            l = row
            l.sort(reverse=True)
            # print(l)
            for j in range(limits[i]):
                list.append(l[j])
            i+=1
        list.sort(reverse=True)
        # print(list)
        return sum(list[0:k])