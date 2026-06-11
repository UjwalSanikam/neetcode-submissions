class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest = 1
        runlength = 1
        if nums == []:
            return 0
        for i in range(len(sorted_nums) - 1):
            if(sorted_nums[i] + 1 == sorted_nums[i+1]):
                runlength = runlength + 1
            elif(sorted_nums[i] == sorted_nums[i+1]):
                continue
            else:
                if runlength > longest:
                    longest = runlength
                    runlength = 1
                else:
                    runlength = 1
        return max(longest, runlength)
            
            
        