class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height) - 1
        left = 0
        right = length

        leftMax = height[left]
        rightMax = height[right]

        if length == 0:
            return 0

        water = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                print("Left" + str(left))
                water += leftMax - height[left]
                print(water)
                

            else:
                right -=1
                rightMax = max(height[right], rightMax)
                print("Right" + str(right))
                water += rightMax - height[right]
                print(water)
                

        return water
        