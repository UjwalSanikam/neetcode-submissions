class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        nums.sort()
        i = 0
        while i < len(nums):
            runlength = 1
            runvalue = nums[i]
            j = i
            while j < len(nums)-1 and nums[j] == nums[j+1]:
                runlength = runlength + 1
                j = j + 1
            dict1[runvalue] = runlength
            i = i + runlength
        dict_sorted = sorted(dict1, key = lambda value: dict1[value], reverse = True)
        final_list = []
        for p in range(k):
            final_list.append(dict_sorted[p])
        return final_list