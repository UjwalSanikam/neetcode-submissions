class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in range (len(strs)):
            tuple1 = tuple(sorted(list(strs[i])))
            if tuple1 in dict1:
                dict1[tuple1].append(strs[i])
            else:
                dict1[tuple1] = []
                dict1[tuple1].append(strs[i])
        return list(dict1.values())

            
                    