class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "!" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while (i < len(s)):
            j = i
            # get length
            while s[j] != "!":
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1: length + j + 1])
            i = length + j + 1
        return res
