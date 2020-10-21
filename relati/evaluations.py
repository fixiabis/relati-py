from relati.rules import isPlaceable, isRelatiPlaceable
from relati.routes import normalRoutes


def evaluatePlayerPoints(symbol, board):
    points = 0
    opponentSymbol = (symbol + 1) % 2
    isGridPlaceable = map(isPlaceable, board.grids)

    isGridRelatiPlaceableForSymbol = [
        isRelatiPlaceable(grid, symbol) for grid in board.grids
    ]

    isGridRelatiPlaceableForOpponentSymbol = [
        isRelatiPlaceable(grid, opponentSymbol) for grid in board.grids
    ]

    def getPoint(isGridPlaceable, isGridRelatiPlaceableForSymbol, isGridRelatiPlaceableForOpponentSymbol):
        if not isGridPlaceable:
            return 0

        if isGridRelatiPlaceableForSymbol and isGridRelatiPlaceableForOpponentSymbol:
            return 1

        if isGridRelatiPlaceableForSymbol and not isGridRelatiPlaceableForOpponentSymbol:
            return 5

        if not isGridRelatiPlaceableForSymbol and isGridRelatiPlaceableForOpponentSymbol:
            return -5

        return 0

    points = sum(map(
        getPoint,
        isGridPlaceable,
        isGridRelatiPlaceableForSymbol,
        isGridRelatiPlaceableForOpponentSymbol
    ))

    return points


def getGridIndexesOfPlaceableAreas(board):
    gridIndexesOfPlaceableAreas = []

    for grid in board.grids:
        if not isPlaceable(grid):
            continue

        isGridInArea = False
        nearbyGrids = [grid.getGridTo(x, y) for [[x, y]] in normalRoutes]

        for nearbyGrid in nearbyGrids:
            if nearbyGrid is None or not isPlaceable(nearbyGrid):
                continue
            
            for gridIndexesOfPlaceableArea in gridIndexesOfPlaceableAreas:
                if nearbyGrid.index in gridIndexesOfPlaceableArea:
                    gridIndexesOfPlaceableArea.append(grid.index)
                    isGridInArea = True
                    break
            
            if isGridInArea:
                break
        
        if not isGridInArea:
            gridIndexesOfPlaceableArea = [grid.index]
            gridIndexesOfPlaceableAreas.append(gridIndexesOfPlaceableArea)
