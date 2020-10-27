from relati_perf.routes import RELATI_NORMAL_ROUTES, RELATI_ROUTES


class RelatiGrid:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.index = y * board.width + x
        self.symbol = None
        self.status = None
        self.nearbyGrids = []
        self.relatiRoutes = []

    def initAfterBoardReady(self):
        for route in RELATI_ROUTES:
            gridsOfRoute = [
                self.getGridTo(dx, dy)
                for [dx, dy] in route
            ]

            if gridsOfRoute[0] is not None:
                self.relatiRoutes.append(gridsOfRoute)

        for [[dx, dy]] in RELATI_NORMAL_ROUTES:
            nearbyGrid = self.getGridTo(dx, dy)

            if nearbyGrid is not None:
                self.nearbyGrids.append(nearbyGrid)

    def getGridTo(self, x, y):
        dx = self.x + x
        dy = self.y + y
        grid = self.board.getGridAt(dx, dy)
        return grid


class RelatiBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.length = width * height
        self.grids = [None] * self.length

        for x in range(width):
            for y in range(height):
                grid = RelatiGrid(x, y, self)
                self.grids[grid.index] = grid

        for grid in self.grids:
            grid.initAfterBoardReady()

    def getGridAt(self, x, y):
        isOverBoundary = (
            x < 0 or x >= self.width or
            y < 0 or y >= self.height)

        if isOverBoundary:
            return None

        index = y * self.width + x
        grid = self.grids[index]
        return grid
