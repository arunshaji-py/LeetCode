class Solution:
    def maxArea(self, height: list[int]) -> int:
        #define the two pointers
        left = 0
        right = len(height)-1
        max_area = 0

        #define a while to run until we find the heights which gives the maximum area.
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width

            max_area = max(area, max_area)

            #move the shorter pointer inward

            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        
        return max_area