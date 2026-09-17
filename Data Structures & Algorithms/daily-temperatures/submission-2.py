class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack, only push colder temps so stack (temp, index)
        # for each temp, pop off stack until its colder
        # get index by taking curr index and subtracting index in tuple

        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i,t = stack.pop()
                res[i] = index - i
            
            stack.append((index, temp))

        return res
