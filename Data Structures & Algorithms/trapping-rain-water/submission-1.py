class Solution:
    def trap(self, heights: list[int]) -> int:
        if not heights:
            return 0
            
        total_water = 0
        
        for i in range(len(heights)):
            left_max = max(heights[:i+1])
            right_max = max(heights[i:])
            water = min(left_max, right_max) - heights[i]
            
            total_water += water
            
        return total_water