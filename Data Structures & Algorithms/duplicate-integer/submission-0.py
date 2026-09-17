class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevValues = set()
        for n in nums:
            if n in prevValues:
                return True
            prevValues.add(n)
        return False