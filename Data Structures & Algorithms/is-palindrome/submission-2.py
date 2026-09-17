class Solution:
    def isPalindrome(self, s: str) -> bool:

        # palindrome is a word that reads the same forward and backward

        # can use two pointers to solve this problem

        left = 0
        right = len(s) - 1

        while left < right:

            while not s[right].isalnum() and left < right:
                right -= 1
            while not s[left].isalnum() and left < right:
                left += 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

        

        
        