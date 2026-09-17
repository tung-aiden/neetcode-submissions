class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_streak = 0

        for num in nums:
            
            current_streak = 1
            while num + 1 in nums:
                num += 1
                current_streak +=1
            longest_streak = max(longest_streak, current_streak)

        return longest_streak



        