class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack based solution
        # monotic stack, only push elements that have a increasing height
        # if we reach a decreasing height, that is potentially a boundary for previous
        # elements on the stack, so pop from stack and calculate possible areas until the stack is 
        # strictly increasing again
        # areas we calculate are the bar itself, and the boundaries
        # index should be the minimum where it is still valid

        stack = []
        maxA = 0

        for i, h in enumerate(heights):
            # pop and calculate heights
            if stack and stack[-1][1] > h:
                while stack and stack[-1][1] > h:
                    pop_i, pop_h = stack.pop()
                    # boundaries
                    area = (i - pop_i) * pop_h
                    maxA = max(maxA, area) 
                # strictly increasing, add min index where height is valid
                stack.append((pop_i, h))
            else:
                stack.append((i, h))


        # if stack not empty at end, heights were able to fully extend, so compute them 
        length = len(heights)
        while stack:
            i, h = stack.pop()
            area = (length - i) * h
            maxA = max(maxA, area)
        
        return maxA
            
        

                
