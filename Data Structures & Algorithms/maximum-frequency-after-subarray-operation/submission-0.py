class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = nums.count(k)
        max_gain = 0
        unique_nums = set(nums)
        for v in unique_nums:
            if v == k:
                continue
            current_gain = 0
            for num in nums:
                if num == v:
                    current_gain = current_gain + 1
                elif num == k:
                    current_gain = current_gain - 1
                if current_gain < 0:
                    current_gain = 0
                if current_gain > max_gain:
                    max_gain = current_gain
        result = total_k + max_gain
        return result
        