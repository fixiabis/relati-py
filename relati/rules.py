from relati.routes import routes

from relati.types import (
    isRelatiSymbol,
    isRelatiSymbolEqual,
    isRelatiRepeater,
    isRelatiReceiver,
    isRelatiDeceased,
    isRelatiRepeatable,
    toRelatiRepeater,
    toRelatiReceiver,
)


def isPlaceable(grid):
    return grid.body is None


def isPenetrable(grid):
    return grid.body is None or isRelatiDeceased(grid.body)


def isRelatiPlaceable(grid, symbol):
    for route in routes:
        [sourceGrid, *gridsInRoute] = [grid.getGridTo(x, y) for x, y in route]

        isSourceGridReliable = (
            sourceGrid is not None and
            sourceGrid.body is not None and
            isRelatiSymbol(sourceGrid.body, symbol) and
            isRelatiRepeatable(sourceGrid.body)
        )

        if not isSourceGridReliable:
            continue

        isRouteAvailable = all(map(isPenetrable, gridsInRoute))

        if not isRouteAvailable:
            continue

        return True

    return False


def disablePieces(board):
    for grid in board.grids:
        if grid.body is not None and isRelatiRepeater(grid.body):
            grid.body = toRelatiReceiver(grid.body)


def enablePieces(grid):
    for route in routes:
        [targetGrid, *gridsInRoute] = [grid.getGridTo(x, y) for x, y in route]

        isTargetGridPending = (
            targetGrid is not None and
            targetGrid.body is not None and
            isRelatiSymbolEqual(targetGrid.body, grid.body) and
            isRelatiReceiver(targetGrid.body)
        )

        if not isTargetGridPending:
            continue

        isRouteAvailable = all(map(isPenetrable, gridsInRoute))

        if not isRouteAvailable:
            continue

        targetGrid.body = toRelatiRepeater(targetGrid.body)
        enablePieces(targetGrid)


def getGameStatus(turn, board):
    isAllRootPlaced = turn >= 2

    if not isAllRootPlaced:
        return False, -1

    movablePlayersCount = 0

    while movablePlayersCount != 2:
        symbol = turn % 2

        isGridPlaceable = any([
            isPlaceable(grid) and isRelatiPlaceable(grid, symbol)
            for grid in board.grids
        ])

        if isGridPlaceable:
            if movablePlayersCount == 2 - 1:
                return True, symbol

            return False, -1
        else:
            turn += 1

        movablePlayersCount += 1

    if movablePlayersCount == 2:
        return True, -1
