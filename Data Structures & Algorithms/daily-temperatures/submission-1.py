class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        # use a monotomically decreasing stack
        stack = []

        for i in range(len(temperatures)):
            # stack is empty
            if not stack:
                # store temperature and also the index
                stack.append([temperatures[i], i])
            # current temp is less than/equal to temps in stack
            elif temperatures[i] <= int(stack[-1][0]):
                stack.append([temperatures[i], i])
            # current temp is greater than all temps in the stack
            else:
                print(stack)
                while stack and temperatures[i] > stack[-1][0]:
                    temp = stack.pop()
                    index = temp[1]
                    days = i - index
                    result[index] = days
                stack.append([temperatures[i], i])
        return result
                




        


