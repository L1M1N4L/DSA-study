class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if abs((j - i)) * min(heights[j],heights[i]) > max_water:
                    max_water = (j - i) * min(heights[j],heights[i])
        return max_water


        