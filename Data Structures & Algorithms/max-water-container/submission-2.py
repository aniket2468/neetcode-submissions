class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            area = max(area, curr_area)
            if heights[l] > heights[r]:
                r -=  1
            else:
                l += 1
        return area