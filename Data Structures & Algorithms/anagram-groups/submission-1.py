class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # task here is to group all the anagrams together into sublists

        anagram_dict = defaultdict(list)

        for word in strs:
            list_string = list(word)
            list_string.sort()
            anagram = "".join(list_string)
            anagram_dict[anagram].append(word)
        return anagram_dict.values()

        