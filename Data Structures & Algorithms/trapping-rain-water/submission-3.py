class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        # we don't need an external array, we only care about the min of the two heights
        # so if we shift L, we know thats lower than whaterever is on the right so we can disregard
        # since L would be the bottleneck

        water = 0
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            if maxL <= maxR:
                water += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                water += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
        
        return water