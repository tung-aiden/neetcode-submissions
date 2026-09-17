class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # two maps
        # each tracking character counts in s and t

        sMap, tMap = defaultdict(int), defaultdict(int)

        # if the s map != t map == False else True
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        
        return True if sMap == tMap else False