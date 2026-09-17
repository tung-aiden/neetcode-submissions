class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                return False
            elif char in char_dict:
                if char_dict[char] == 0:
                    return False
                else:
                    char_dict[char] -= 1

        return True

  
        