class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we can use binary search
        # we can start with the mid value, and see if the mid value is part of the rotated array or not

        right = len(nums) - 1
        left = 0
        # init the result to the left most value
        result = nums[0]

        while left <= right:
            mid = (left + right) // 2
            # this means the array is in sorted order
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            # we are in the rotated part of the array
            result = min(result, nums[mid])
            if nums[mid] >= nums[right]:
                left= mid + 1
            else:
                right = mid - 1
            
        return result


        