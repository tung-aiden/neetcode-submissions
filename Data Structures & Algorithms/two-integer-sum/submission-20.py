class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in sums and i != sums[diff]):
                return([sums[diff], i])
            sums[nums[i]] = i
                

        
        