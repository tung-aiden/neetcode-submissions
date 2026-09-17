class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # monotonicaly increasing stack
        # sort pairs by position
        cars = sorted(list(zip(position, speed)), key = lambda x:x[0], reverse = True)
        # go through pairs in reverse position
        # push time onto stack
        stack = []
        for p, s in cars:
            # calculate time to target, if greater than top of stack
            time = (target - p) / s
            if not stack:
                stack.append(time)
            elif stack and time > stack[-1]:
                stack.append(time)

        # return length of the stack = car fleets
        return len(stack)
