class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums
        # iertae through, check if current - 1 is in set, if not its start of seq
        #only hit each number once

        numSet = set(nums)

        maxL = 0
        for n in numSet:
            if n - 1 in numSet:
                continue
            
            # start of seq
            length = 0
            curr = n
            while curr in numSet:
                length += 1
                maxL = max(maxL, length)
                curr += 1

        return maxL