class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # there will be two sections of sorted arrays because of the rotattion
        # I can use this with binary search to cut out parts of the arrays

        # all numbers in nums are unique
        # [3,4,5,6,1,2]

        left = 0
        right = len(nums) - 1
        result = -1

        # [ 5, 1, 2, 3, 4]

        while left <= right:
            mid = (left + right) // 2
            print("Mid: " + str(nums[mid]))
            if nums[mid] == target:
                return mid
            # middle number is greater than left pointer
            # this part of the array is sorted
            if nums[mid] >= nums[left]:
                if nums[mid] < target or nums[left] > target:
                    print("Left: " + str(nums[left]))
                    left = mid + 1
                else:
                    right = mid - 1
                    print("Right: " + str(nums[right]))
            # [4, 5, 1, 2, 3]
            # this array is not sorted, mid < left
            else:
                if nums[right] < target or target < nums[mid]:
                    right = mid - 1
                #if nums[right] > target
                else:
                    left = mid + 1
        return result




        