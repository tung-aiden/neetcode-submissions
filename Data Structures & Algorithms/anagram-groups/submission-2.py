class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}

        for s in strs:
            s_arr = list(s)
            s_arr.sort()
            ana = "".join(s_arr)
            if ana in mp:
                mp[ana].append(s)
            else:
                mp[ana] = [s]
        
        return mp.values()
        