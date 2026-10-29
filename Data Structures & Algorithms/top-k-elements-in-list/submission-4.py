class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #iterate through nums and create a frequency map of ints 1 - 9 and count how many times each one appears than return the ints that correspond to the values >= k 
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freqs[c].append(n)
        result = [] 
        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                result.append(n)
                if len(result) == k:
                    return(result)


