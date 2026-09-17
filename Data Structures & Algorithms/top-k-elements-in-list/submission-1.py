class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to get a count number : frequency
        # init a map of length of nums frequency : number
        # loop thru backwards

        # O(n)
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        # O(n)
        freqArr = [[] for _ in range(len(nums) + 1)]
        for n, freq in count.items():
            freqArr[freq].append(n)

        # O()
        res = []
        for i in range(len(freqArr) - 1, -1, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
        
