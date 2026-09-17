class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0

        # init pointers
        left = 0
        right = len(height) - 1

        # set the initial left max and right max
        leftMax = height[left]
        rightMax = height[right]

        result = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]

        return result
        