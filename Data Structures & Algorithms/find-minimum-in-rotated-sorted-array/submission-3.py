class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we can use binary search
        # we can start with the mid value, and see if the mid value is part of the rotated array or not

        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            # calculate mid value
            mid = (left + right) // 2
            result = min(result, nums[mid])

            # sorted part
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return result






        