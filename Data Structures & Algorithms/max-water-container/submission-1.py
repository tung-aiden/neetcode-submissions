class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # array -> heights
        # we want to return the max area

        # we want to keep the max height

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            min_height = min(heights[left], heights[right])
            current_area = min_height * (right - left)
            max_area = max(current_area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
    