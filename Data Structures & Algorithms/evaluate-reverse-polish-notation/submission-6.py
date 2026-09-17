class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack approach
        # push token onto stack until operand, pop two ops off stack
        # perform op, push back onto stack
        # truncate towards zero -> cast to int

        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a) + int(b))
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a) * int(b))
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int((int(b) / int(a))))
            else:
                stack.append(t)
        
        return int(stack[-1])          