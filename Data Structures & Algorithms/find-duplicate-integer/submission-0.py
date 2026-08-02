class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_list = []
        for i in range(len(nums)):
            if nums[i] in new_list:
                return nums[i]
            new_list.append(nums[i])

        