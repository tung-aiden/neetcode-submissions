class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res



    def decode(self, s: str) -> List[str]:
        print(s)
        
        i = 0
        j = 0
        res = []

        while i < len(s):

            while s[j] != "#":
                j += 1
            length = s[i:j]
            print(length)
            i = j + 1
            j = i + int(length)
            res.append(s[i:j])
            i = j
        return res
    

