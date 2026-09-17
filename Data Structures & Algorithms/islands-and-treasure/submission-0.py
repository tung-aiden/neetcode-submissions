class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(grid, queue, visit):
            length = 1
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        curR, curC = r + dr, c + dc
                        if min(curR, curC) < 0 or curR == ROWS or curC == COLS or (curR, curC) in visit or grid[curR][curC] != 2147483647:
                            continue
                        
                        visit.add((curR, curC))
                        queue.append((curR, curC))
                        grid[curR][curC] = length

                length += 1

            
            return grid
                
        
        """
        loop through grid, add treasure to the queue/visit
        perform bfs adding the cur length to each INF cell
        return the grid
        """
        queue = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        
        bfs(grid, queue, visit)
                


        




