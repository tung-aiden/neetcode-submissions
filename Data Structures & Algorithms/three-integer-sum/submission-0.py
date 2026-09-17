class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the list
        nums.sort()

        result = []

        # go through each number in the list
        for i in range(len(nums)):
            # init the end pointer
            k = len(nums) - 1
            # init the next pointer
            j = i + 1

            while j < k:

                if (nums[i] + nums[j] + nums[k]) == 0:
                    if ([nums[i], nums[j], nums[k]] not in result):
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
                




        