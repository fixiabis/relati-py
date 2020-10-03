class Grid:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.index = y * board.width + x
        self.body = None

    def getGridTo(self, x, y):
        dx = self.x + x
        dy = self.y + y
        grid = self.board.getGridAt(dx, dy)
        return grid


class GridBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.length = width * height
        self.grids = [None] * self.length

        for x in range(height):
            for y in range(width):
                grid = Grid(x, y, self)
                self.grids[grid.index] = grid

    def getGridAt(self, x, y):
        isOverBoundary = (
            x < 0 or x >= self.width or
            y < 0 or y >= self.height)

        if isOverBoundary:
            return None

        index = y * self.width + x
        grid = self.grids[index]
        return grid
