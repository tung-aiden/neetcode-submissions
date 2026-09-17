class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {i:nums[i] for i in range(len(nums))}

        for i in range(len(nums)):
            difference = target - nums[i]
            for key, value in numMap.items():
                if value == difference and key != i:
                    return [i,key]   



        