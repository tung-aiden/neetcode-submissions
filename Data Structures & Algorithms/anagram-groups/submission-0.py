class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # task here is to group all the anagrams together into sublists

        anagram_dict = {}

        for word in strs:
            list_word = list(word)
            list_word.sort()
            anagram = "".join(list_word)
            if anagram in anagram_dict:
                anagram_dict[anagram].append(word)
            else:
                anagram_dict[anagram] = [word]

        return anagram_dict.values()

        