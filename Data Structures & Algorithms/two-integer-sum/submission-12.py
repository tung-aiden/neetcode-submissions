class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of prev nums, if target - curr is in prev set, return those indices
        # keep track of num : indice

        prev = {}

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in prev:
                return [prev[diff], i]
            
            prev[curr] = i
        
