class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        list = []
        for i, j in dict.items():
            list.append((j, i))
        list.sort(reverse = True)
        print(list)
        new_list = []
        for i in range(k):
            i, j = list[i]
            new_list.append(j)
        return new_list
