from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    my_grid = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(len(my_grid)):
        for j in range(len(my_grid[0])):
            my_grid[i][j] = value
    return(my_grid)


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
