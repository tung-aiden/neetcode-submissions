class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # to achieve O(n), can take the array, multiply everything to the right of it,
        # then multiply everything to the left of it

        product = [1] * len(nums)
        # multiplying everything to the left of each num in the array
        for i in range(1, len(nums)):
            product[i] = nums[i - 1] * product[i - 1]
        print(product)

        # now multiply everything to the right of each num in the array
        #len(nums) is one more than indexes
        # furthest right has no numbers to its right - start at len(nums) - 2

        # grab the most right num
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            product[i] = right * product[i]
            right = right * nums[i]

        return product

        

        