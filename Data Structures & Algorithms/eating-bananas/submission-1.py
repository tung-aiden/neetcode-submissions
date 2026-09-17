class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # the max number of bananas will be the largest num of bananas in pile
        # min will be eating 1 banana
        left = 1
        right = max(piles)
        bananas = 0
        # binary search on the num of bananas 1 : max(piles)
        while left <= right:
            # init time
            time = 0
            # calculate the mid
            mid = (left + right) // 2

            # go through ecah pile
            for pile in piles:
                # calculate the time to finish current pile of bananas with current mid
                time += math.ceil(float(pile) / mid)
            # if the time calculated is less than/equal to hours, reduce right pointer
            if time <= h:
                # store the current result
                bananas = mid
                right = mid - 1
            # koko needs more time
            else:
                left = mid + 1
        return bananas



        