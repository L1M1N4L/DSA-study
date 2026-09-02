class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        max_water = min(heights[l] , heights[r]) * (r - l)
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = min(heights[l], heights[r]) * (r - l)
            max_water = max(area , max_water)
        
        return max_water

