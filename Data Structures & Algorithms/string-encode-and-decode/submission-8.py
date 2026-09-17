class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word))
            s += '!'
            s+= word
        print(s)
        return s

    def decode(self, s: str) -> List[str]:

        left = 0
        right = 0
        res = []

        while left < len(s):
            right = left
            while s[right] != '!':
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            res.append(s[left:right])
            left = right

        return res
