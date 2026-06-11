class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                water = width * height
                if water > max_water:
                    max_water = water
        return max_water
        