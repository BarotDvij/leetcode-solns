# Last updated: 10/15/2025, 3:07:36 AM
class Solution(object):
    def maxArea(self, height):
        y1, y2 = 0, len(height)-1
        area = ans = min(height[y1], height[y2]) * (y2-y1)

        while y2 > y1:        
            if height[y1] >= height[y2]:
                area = height[y2] * (y2-y1)
                if area > ans:
                    ans = area
                y2 -= 1
            
            else:
                area = height[y1] * (y2-y1)
                if area > ans:
                    ans = area
                y1 += 1
            
        return ans