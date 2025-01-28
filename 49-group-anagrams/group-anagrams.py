class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            i_sort = "".join(sorted(i))
            #print(i_sort)
            if i_sort not in dict:
                dict[i_sort] = [i]
            else:
                dict[i_sort].append(i)
        list = []
        for i in dict.values():
            list.append(i)
        return list