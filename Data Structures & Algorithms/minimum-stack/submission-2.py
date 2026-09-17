class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        # at each state of adding a value, we can keep track of the current min
        # latest val in minStack will be the smallest value
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def getMin(self):
        return self.minStack[-1]


        
