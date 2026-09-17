class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for each column and row and sub box, create a set
        # iterate through the board, if the num alr in the set return false else true
        # map c,r,subbox : set of numbers appeared
        # to get the subbox, we can take the r // 3, c // 3

        columns = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]

                if curr == ".":
                    continue

                if curr in columns[c] or curr in rows[r] or curr in boxes[(r // 3, c // 3)]:
                    return False

                columns[c].add(curr)
                rows[r].add(curr)
                boxes[(r // 3, c // 3)].add(curr)


        return True