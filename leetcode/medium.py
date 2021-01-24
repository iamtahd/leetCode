from typing import List


def numIslands(grid: List[List[str]]):
    """
    Given an m x n 2d grid map of '1's (land) and '0's (water),
    return the number of islands.

    LeetCode problem # 200:
        An island is surrounded by water and is formed by connecting
        adjacent lands horizontally or vertically. You may assume all
        four edges of the grid are all surrounded by water.

    :examples:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3

    :param grid:
    :return:
    """

    def dfs(grid_, i_, j_):
        if 0 <= i_ < m and 0 <= j_ < n and grid_[i_][j_] == "1":
            grid[i_][j_] = "2"
            dfs(grid_, i_ - 1, j_)
            dfs(grid_, i_ + 1, j_)
            dfs(grid_, i_, j_ - 1)
            dfs(grid_, i_, j_ + 1)

    if not grid:
        return 0

    m, n, islands = len(grid), len(grid[0]), 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                islands += 1
                dfs(grid, i, j)

    return islands
