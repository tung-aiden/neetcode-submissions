class Solution:
    # here is a design algoriothm question
    # to encode, want to know the length of each string
    # use a character => "# " to separate strings, and have the string
    def encode(self, strs: List[str]) -> str:

        joined_string = ""
        for string in strs:
            joined_string += str(len(string)) + "#" + string

        print(joined_string)
        return joined_string


    def decode(self, s: str) -> List[str]:

        length = len(s)

        starting_index = 0
        modify_index = 0
        result = []

        while starting_index < length:

            while s[starting_index] != "#":
                starting_index += 1

            # get the current len of string
            curr_str_len = int(s[modify_index:starting_index])
            # set the modify index to the last char in the string
            modify_index = starting_index + curr_str_len + 1
            # move starting index up 1 to not capture "#"
            starting_index += 1
            # add the string
            result.append(s[starting_index:modify_index])
            # move starting index to where we left off
            starting_index = modify_index

        return result