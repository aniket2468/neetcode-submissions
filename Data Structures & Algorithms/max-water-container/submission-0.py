class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            temp = min(heights[left], heights[right]) * (right - left)
            res = max(res, temp)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res


        