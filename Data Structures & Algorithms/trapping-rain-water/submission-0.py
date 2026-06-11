class Solution:
    def trap(self, heights: list[int]) -> int:
        if not heights:
            return 0
            
        total_water = 0
        
        for i in range(len(heights)):
            # Find the absolute tallest bar to the left (including itself)
            left_max = max(heights[:i+1])
            
            # Find the absolute tallest bar to the right (including itself)
            right_max = max(heights[i:])
            
            # Water above this block is the min of the two tallest boundary walls, 
            # minus the height of the block itself
            water = min(left_max, right_max) - heights[i]
            
            total_water += water
            
        return total_water