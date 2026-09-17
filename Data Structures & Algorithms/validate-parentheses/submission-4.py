class Solution:
    def isValid(self, s: str) -> bool:
        # push open brackets onto stack
        # when we hit a closed bracket -> pop top of stack and verify its matching
        # stack must be empty at end if everything had a match

        closedToOpen = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        for p in s:
            if stack and p in closedToOpen:
                top = stack.pop()
                if top != closedToOpen[p]:
                    return False
            else:
                stack.append(p)

        
        return False if stack else True
