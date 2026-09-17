class Solution:
    def isValid(self, s: str) -> bool:

        mapping_dict = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:
            # closing char
            if char in mapping_dict:
                if not stack:
                    return False
                open_char = stack[-1]
                if str(open_char) != mapping_dict[char]:

                    return False
                stack.pop()
            
            else:
                # it is an opening char
                # add it to the stack
                stack.append(char)

        return not stack
        
        