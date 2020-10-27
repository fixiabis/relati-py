from relati_perf.types import (
    RELATI_DECEASED,
    RELATI_RECEIVER,
    RELATI_REPEATER,
)


def isPlaceable(grid):
    return grid.symbol is None


def isPenetrable(grid):
    return isPlaceable(grid) or grid.status == RELATI_DECEASED


def isRelatiable(grid, symbol):
    for [sourceGrid, *gridsInRoute] in grid.relatiRoutes:
        isSourceGridReliable = (
            sourceGrid.symbol == symbol and
            sourceGrid.status <= RELATI_REPEATER
        )

        if not isSourceGridReliable:
            continue

        isRouteAvailable = all(map(isPenetrable, gridsInRoute))

        if isRouteAvailable:
            return True

    return False


def isRelatiPlaceable(grid, symbol):
    return isPlaceable(grid) and isRelatiable(grid, symbol)


def reEnablePieces(board):
    for grid in board.grids:
        if grid.status == RELATI_REPEATER:
            grid.status = RELATI_RECEIVER

    isAllEnabled = False

    while not isAllEnabled:
        isAllEnabled = True

        for grid in board.grids:
            if isPlaceable(grid) or grid.status != RELATI_RECEIVER:
                continue

            if isRelatiable(grid, grid.symbol):
                grid.status = RELATI_REPEATER
                isAllEnabled = False


def getGameStatus(turn, board):
    if turn < 2:
        return False, -1

    movablePlayersCount = 0

    while movablePlayersCount != 2:
        symbol = turn % 2

        isGridPlaceable = any([
            isRelatiPlaceable(grid, symbol)
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
