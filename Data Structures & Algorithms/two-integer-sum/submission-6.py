class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(1,len(nums)):
                if nums[x] + nums[y] == target and x != y:
                    return [x,y]
                      



        