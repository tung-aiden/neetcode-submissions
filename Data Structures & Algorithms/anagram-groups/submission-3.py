class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use the valid anagram code to check if something is an anagram 
        #then use a nested for loop to iterate through the code checking if the first word 
        #is an anagram of any other words and if so make note of indexes and store index 
        #position in an array, then cross check with array and any value not in array check it 
        #with other values not in array then check those values till all values have been checked
        res = defaultdict(list)
        for s in strs: 
            count = [0] * 26 
            for c in s: 
                count[ord(c) - ord("a")] += 1 
            res[tuple(count)].append(s)
        return list(res.values()) 
            
