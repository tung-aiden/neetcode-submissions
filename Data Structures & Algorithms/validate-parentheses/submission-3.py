class Solution:
    def isValid(self, s: str) -> bool:

        mapping_dict = {")" : "(", "]" : "[", "}" : "{"}

        stack = []

        for char in s:

            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != mapping_dict[char]:
                    return False
        if stack:
            return False
        
        return True
        
        