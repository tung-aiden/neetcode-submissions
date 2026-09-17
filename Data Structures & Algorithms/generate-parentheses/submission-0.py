class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # n = num_open = num_close
        # we always know that num_open has to be greater than num_close in current state
        res = []

        def backtrack(open_count, close_count, string):
            print(f"backtrack called with open_count={open_count}, close_count={close_count}, string='{string}'")

            # base case: added n closing and n open parenthesis
            if len(string) == (2 * n):
                print(f"Added to result: {string}")  # Debug: Base case hit
                res.append(string)
            
            # add open parthensis while still valid
            if open_count < n:
                # call backtrack with next iteration
                backtrack(open_count + 1, close_count, string + "(")
            
            # add closing parenthesis only if close_count < open_count
            if close_count < open_count:
                print(f"Adding ')': close_count={close_count}, string='{string}'")  # Debug
                backtrack(open_count, close_count + 1, string + ")")

        backtrack(0, 0, "")

        return res



        