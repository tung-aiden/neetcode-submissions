class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force method
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(len(temperatures)):
                if j < i:
                    continue
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result

        


