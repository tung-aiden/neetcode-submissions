class Solution:
    # here is a design algoriothm question
    # to encode, want to know the length of each string
    # use a character => "# " to separate strings, and have the string
    def encode(self, strs: List[str]) -> str:
        # initialize an empty string
        joined_str = ""
        # will use the legnth of the string, followed by a '#' as a separator, then the string
        for s in strs:
            joined_str += str(len(s)) + "#" + s

        print(joined_str)
        return joined_str


    def decode(self, s: str) -> List[str]:

        # use two indexes, to add strings
        start_index = 0
        modify_index = 0

        result = []

        while start_index < len(s):

            # we know there is a '#' followed by the length of each str
            # go until we find the length
            while s[modify_index] != '#':
                modify_index += 1
            # getting the length of our current string
            len_str = s[start_index:modify_index]
            # set the starting index to first char in string
            start_index = modify_index + 1
            # set the modify_index to last char in string
            modify_index += int(len_str) + 1
            result.append(s[start_index:modify_index])
            print(result)
            # set the starting index to where we left off
            start_index = modify_index

        return result