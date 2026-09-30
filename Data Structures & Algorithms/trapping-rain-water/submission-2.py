class Solution:
    def trap(self, height: List[int]) -> int:
        # pre and post array to find max boundaries of both sides
        # then for each, min(maxL, maxR) - hieght = water in spot
        # O(n) time O(n) space where n is number of heights

        prefix = [0] * len(height)
        postfix = [0] * len(height)

        # pre
        maxH = height[0]
        for i, h in enumerate(height):
            maxH = max(maxH, h)
            prefix[i] = maxH
        
        # post
        maxH = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            maxH = max(maxH, height[i])
            postfix[i] = maxH
        
        total_water = 0
        for i in range(len(height)):
            water = min(prefix[i], postfix[i]) - height[i]
            if water > 0:
                total_water += water
        
        return total_water