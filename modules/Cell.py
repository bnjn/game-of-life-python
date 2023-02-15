from collections import Counter


class Cell():
    
    def __init__(self) -> None:
        self.alive = True

    def die(self) -> None:
        self.alive = False

    # TODO: Refeactor this abomination.
    def check_living_neighbours(self, grid) -> int:
        for row in grid:
            for cell in row:
                if cell == self:
                    y = grid.index(row)
                    x = row.index(self)
                    neighbouring_cells = []
                    if x-1 < 0 and y-1 < 0:
                        # Top left corner
                        try:
                            neighbouring_cells.append(row[x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x])
                        except IndexError:
                            pass
                    elif x-1 < 0:
                        # Left edge
                        try:
                            neighbouring_cells.append(grid[y - 1][x])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y - 1][x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(row[x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x + 1])
                        except IndexError:
                            pass
                    elif y-1 < 0:
                        # Top edge
                        try:
                            neighbouring_cells.append(row[x - 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(row[x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x + 1])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x - 1])
                        except IndexError:
                            pass
                    else:
                        # Try to catch if on right edge or center
                        try:
                            neighbouring_cells.append(row[x + 1])
                        except IndexError:
                            pass                            
                        try:
                            neighbouring_cells.append(grid[y + 1][x])
                        except IndexError:
                            pass
                        try:
                            neighbouring_cells.append(grid[y + 1][x + 1])
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

                        neighbouring_cells.append(grid[y - 1][x])
                        neighbouring_cells.append(row[x - 1])
                        neighbouring_cells.append(grid[y - 1][x - 1])


                    if None in neighbouring_cells:
                        return len([cell for cell in neighbouring_cells if cell != None])
                    return len(neighbouring_cells)