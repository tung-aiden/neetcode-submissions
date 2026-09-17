class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 + num2
                stack.append(num3)

            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num2 - num1
                stack.append(num3)

            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = int(num2 / num1)
                stack.append(num3)

            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 * num2
                stack.append(num3)

            else:
                # integer
                stack.append(int(token))
    
        return stack[-1]
