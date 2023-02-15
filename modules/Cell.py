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
                    neighbouring_cells = []
                    try:
                        neighbouring_cells.append(row[x + 1])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(row[x - 1])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y + 1][x])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y - 1][x])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y + 1][x + 1])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y - 1][x - 1])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y - 1][x + 1])
                    except IndexError:
                        pass
                    try:
                        neighbouring_cells.append(grid[y + 1][x - 1])
                    except IndexError:
                        pass
                    return len(Counter(neighbouring_cells)) - 1