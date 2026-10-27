class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for s in strs:
            freq = [0] * 26 
            for c in s: 
                freq[ord(c) - ord('a')] += 1 
            anas[tuple(freq)].append(s)
        return list(anas.values())
        