class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # run two pointer search on right side of array, move left pointer up one if 
        # < 0 or if same as prev, right pointer down one if > 0 or if same as prev
        # after finding all pairs, move the left pointer over to unique num
        # run until left pointer is len - 2

        nums.sort()

        output = []
        start = 0
        while start < (len(nums) - 2):
            if start != 0 and nums[start] == nums[start - 1]:
                start += 1
                continue

            l, r = start + 1, len(nums) - 1
            while l < r:
                res = nums[start] + nums[l] + nums[r]
                if res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    output.append([nums[start], nums[l], nums[r]])
                    l += 1
                    # move left pointer until not matching prev
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
            start += 1
        
        return output
            
            
