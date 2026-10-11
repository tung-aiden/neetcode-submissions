class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # hours per pile = round up(p / h) 11 / 2 = 5.5 hours -> 6 hours
        # k = [1 .. max(piles)] -> len(piles) time
        # bin search through 1 max(piles) -> less than h -> try slower else try faster

        l, r = 1, max(piles)
        minK = r
        while l <= r:
            k = (l + r) // 2
            totalH = 0
            for p in piles:
                # calc hours per pile
                hours = math.ceil(p / k)
                totalH += hours
            
            if totalH <= h:
                minK = k
                r = k - 1
            else:
                l = k + 1
        
        return minK

