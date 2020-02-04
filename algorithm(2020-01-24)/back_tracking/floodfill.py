class FloodFill:

    def __init__(self):
        self.visited = []
        self.m = 0
        self.n = 0
        self.d = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]

    def num_islands(self, grid):
        res = 0
        self.m = len(grid)
        if not self.m:
            return res
        self.n = len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and not self.visited[i][j]:
                    res += 1
                    self.flood_fill(grid, i, j)
        return res

    def flood_fill(self, grid, start_x, start_y):
        self.visited[start_x][start_y] = True
        for i in self.d:
            new_x = start_x + i[0]
            new_y = start_y + i[1]
            if self.in_area(new_x, new_y) and not self.visited[new_x][new_y] and grid[new_x][new_y] == 1:
                self.flood_fill(grid, new_x, new_y)
        return

    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n


if __name__ == '__main__':
    f = FloodFill()
    grid = [
        [1, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ]

    res = f.num_islands(grid)
    print(res)