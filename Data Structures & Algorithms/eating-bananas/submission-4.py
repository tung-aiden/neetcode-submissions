import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # max number of bananas koko can eat is max(piles)
        # we can do binary search on number of bananas, and see if we can go lower

        left = 1
        right = max(piles)
        bananas = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                print(mid)
                hours += math.ceil(float(pile / mid))
            print(hours)
            if hours <= h:
                bananas = mid
                right = mid - 1
            else:
                left = mid + 1
        return bananas



        