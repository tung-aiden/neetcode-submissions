class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            letters[sortedS].append(s)
        return list(letters.values())
