class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token == "+":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = val1 + val2
                stack.append(res)

            elif token == "-":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = val2 - val1
                stack.append(res)

            elif token == "*":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = val1 * val2
                stack.append(res)

            elif token == "/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = val2 / val1
                stack.append(res)
            # it is a number
            else:
                stack.append(token)
                print(stack[-1])

        return int(stack[-1])

        