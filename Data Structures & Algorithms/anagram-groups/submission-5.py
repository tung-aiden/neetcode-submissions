class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 26 possible characters
        # for each input string, count the number of chracters in each string
        # map cc array : input strings, return the list of input strings
        # time: O(n), space: O(n)

        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        
        return list(groups.values())
        