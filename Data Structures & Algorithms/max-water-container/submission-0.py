class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        
        max_water = 0
        while left < right:
            width = right - left 
            if max_water < width * min(heights[left], heights[right]):
                max_water = width * min(heights[left], heights[right])
            if min(heights[left], heights[right]) == heights[left]:
                left = left +1
            else:
                right = right -1
        
        return max_water 
            
    
        