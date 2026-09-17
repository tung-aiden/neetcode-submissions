class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}


        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in s_dict:
                s_dict[letter] -= 1

        for key in s_dict:
            if s_dict[key] > 0:
                return False
        return True

  
        