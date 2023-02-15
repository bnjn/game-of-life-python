from collections import Counter


class Cell():
    
    def __init__(self) -> None:
        self.alive = True

    def die(self) -> None:
        self.alive = False

    def check_living_neighbours(self, grid) -> int:
        for row in grid:
            for cell in row:
                if cell == self:
                    y = grid.index(row)
                    x = row.index(self)
                    neighbouring_cells = [
                        row[x + 1], # right
                        row[x - 1], # left
                        grid[y + 1][x], # down
                        grid[y - 1][x], # up
                        grid[y - 1][x - 1], # up left
                        grid[y - 1][x + 1], # up right
                        grid[y + 1][x - 1], # down left
                        grid[y + 1][x + 1] # down right
                    ]
                    return len(Counter(neighbouring_cells)) - 1